from app import mongo
from bson import ObjectId
from datetime import datetime
import os

class Server:    
    
    @staticmethod
    def find_all():
        """Récupérer toute les versions"""
        servers = os.listdir("server/")
        return servers
    
    @staticmethod
    def find_by_version(versions):
        """Récupérer par versions"""
        servers = os.listdir("server/")


        return servers
    
