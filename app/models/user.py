from app import mongo
from bson import ObjectId
from datetime import datetime

class User:
    collection = mongo.db.users
    
    @staticmethod
    def create(data):
        """Créer un nouvel utilisateur"""
        user = {
            'name': data.get('name'),
            'email': data.get('email'),
            'age': data.get('age'),
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow()
        }
        result = User.collection.insert_one(user)
        user['_id'] = str(result.inserted_id)
        return user
    
    @staticmethod
    def find_all():
        """Récupérer tous les utilisateurs"""
        users = list(User.collection.find())
        for user in users:
            user['_id'] = str(user['_id'])
        return users
    
    @staticmethod
    def find_by_id(user_id):
        """Récupérer un utilisateur par ID"""
        try:
            user = User.collection.find_one({'_id': ObjectId(user_id)})
            if user:
                user['_id'] = str(user['_id'])
            return user
        except:
            return None
    
    @staticmethod
    def update(user_id, data):
        """Mettre à jour un utilisateur"""
        try:
            update_data = {
                '$set': {
                    'name': data.get('name'),
                    'email': data.get('email'),
                    'age': data.get('age'),
                    'updated_at': datetime.utcnow()
                }
            }
            result = User.collection.update_one(
                {'_id': ObjectId(user_id)},
                update_data
            )
            return result.modified_count > 0
        except:
            return False
    
    @staticmethod
    def delete(user_id):
        """Supprimer un utilisateur"""
        try:
            result = User.collection.delete_one({'_id': ObjectId(user_id)})
            return result.deleted_count > 0
        except:
            return False