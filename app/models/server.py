from app import mongo, client
from bson import ObjectId
from datetime import datetime
import os

class Server:    

    collection = mongo.db.servers
    
    @staticmethod
    def find_all():
        """Récupérer toute les versions"""
        servers = os.listdir("server/")
        return servers
    
    @staticmethod
    def find_by_version(version, one, two, three):
        """Récupérer par versions"""
        servers = os.listdir("server/")


        for s in servers:
            if(version not in s and version != "*"):
                servers.remove(s)
            if(one+"." not in s and one != "*"):
                servers.remove(s)
            if("."+two+"." not in s and two != "*"):
                servers.remove(s)
            if("."+three not in s and three != "*"):
                servers.remove(s)
            
        return servers
    
    @staticmethod
    def create(data):
        """Créer un nouveau serveur"""
        container = client.containers.run(
            "ubuntu:latest",           
            "echo hello world",         
            detach=True                
        )
                
        container_data = {
            "container_id": container.id,
            "container_name": container.name,
            "status": container.status,
            "image": "ubuntu:latest",
            "created_at": datetime.now(),
        }
        
        
        result = Server.collection.insert_one(container_data)
        
        container_obj = {
            "id": str(result.inserted_id),
            "container_id": str(container.id),
            "status": str(container.status)
        }
    
        return container_obj