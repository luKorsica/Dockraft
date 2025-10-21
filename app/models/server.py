from app import mongo, client
from bson import ObjectId
from datetime import datetime
import os

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
        container = client.containers.run(
            data["image"],           
            name=data["name"],    
            detach=True                
        )
                
        container_data = {
            "_id": container.id,
            "container_name": container.name,
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