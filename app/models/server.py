from app import mongo, client
from bson import ObjectId
from datetime import datetime
import os, random
import ansible_runner
import tempfile, subprocess


class Server:    

    collection = mongo.db.servers
    collection_images = mongo.db.images
    
    @staticmethod
    def find_all():
        """Récupérer toute les versions"""
        servers = list(Server.collection_images.find())
        for server in servers:
            server['_id'] = str(server['_id'])
        return servers
    
    @staticmethod
    def find_by_version(version, one, two, three):
        """Récupérer par versions"""
        query = {"mod-loader": version}
        
        if one != "*" and two != "*" and three != "*":
            query["version"] = [int(one), int(two), int(three)]
        
        elif one != "*" and two == "*":
            query["version.0"] = int(one)
        
        elif one != "*" and two != "*" and three == "*":
            query["version.0"] = int(one)
            query["version.1"] = int(two)
                
        servers = list(Server.collection_images.find(query))
        return servers    
    @staticmethod
    def create(data):
        """Créer un nouveau serveur"""

        random_port = random.randint(25000, 65535)

        container = client.containers.run(
            data["image"],           
            name=data["name"],
            ports={'25565/tcp': str(random_port)},
            detach=True                
        )
                
        container_data = {
            "_id": container.id,
            "container_name": container.name,
            "port":str(random_port),
            "status": container.status,
            "image": data["image"],
            "created_at": datetime.now(),
        }
        
        
        result = Server.collection.insert_one(container_data)
        
        container_obj = {
            "id": str(result.inserted_id),
            "container_id": str(container.id),
            "status": str(container.status)
        }
    
        return container_obj
    
    @staticmethod
    def find_server_by_id(id):
        """Récupérer un serveur par ID"""
        try:
            server = Server.collection.find_one({'_id': str(id)})

            container = client.containers.get(id)

            started_at = container.attrs['State']['StartedAt']

            start_time = datetime.fromisoformat(started_at.replace('Z', '+00:00'))
            current_time = datetime.now(start_time.tzinfo)

            uptime = current_time - start_time


            days = uptime.days
            hours, remainder = divmod(uptime.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)            

            if server:
                server['_id'] = str(server['_id'])
                server["status"] = container.status
                server["uptime"] = {
                    "days": days,
                    "hours": hours,
                    "minutes": minutes,
                    "seconds": seconds,
                }
                server["port"] = container.ports
            return server
        except:
            return None
        

    @staticmethod
    def start_server(id):
        """Démarrer un serveur par ID"""
        try:
            container = client.containers.get(id)

            print(container.status)

            if(container.status != "running"):
                container.start()
            else:
                container.stop()
            
            Server.collection.update_one({"_id": str(id)}, {"$set": {"status": container.status}})
            return 
        except:
            return None
        
    
    @staticmethod
    def playbook_server(id, data):
        """Exécuter un playbook sur localhost avec des vars du conteneur"""
        try:
            container = client.containers.get(id)
            
            cmd = [
                'ansible-playbook',
                "payloads/command.yml",
                '-e', f'container_name="{container.name}"',
                '-e', f'command="{data.get("command", "say error")}"'
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            return {
                'success': result.returncode == 0,
                'output': result.stdout
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}