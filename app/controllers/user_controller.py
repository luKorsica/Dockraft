from flask import jsonify, request
from app.models.user import User

class UserController:
    
    @staticmethod
    def get_all_users():
        """Récupérer tous les utilisateurs"""
        try:
            users = User.find_all()
            return jsonify({
                'success': True,
                'data': users,
                'count': len(users)
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @staticmethod
    def get_user(user_id):
        """Récupérer un utilisateur par ID"""
        user = User.find_by_id(user_id)
        if user:
            return jsonify({
                'success': True,
                'data': user
            }), 200
        return jsonify({
            'success': False,
            'error': 'Utilisateur non trouvé'
        }), 404
    
    @staticmethod
    def create_user():
        """Créer un nouvel utilisateur"""
        try:
            data = request.get_json()
            
            # Validation simple
            if not data.get('name') or not data.get('email'):
                return jsonify({
                    'success': False,
                    'error': 'Name et email sont requis'
                }), 400
            
            user = User.create(data)
            return jsonify({
                'success': True,
                'data': user,
                'message': 'Utilisateur créé avec succès'
            }), 201
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @staticmethod
    def update_user(user_id):
        """Mettre à jour un utilisateur"""
        try:
            data = request.get_json()
            
            if not User.find_by_id(user_id):
                return jsonify({
                    'success': False,
                    'error': 'Utilisateur non trouvé'
                }), 404
            
            if User.update(user_id, data):
                return jsonify({
                    'success': True,
                    'message': 'Utilisateur mis à jour avec succès'
                }), 200
            
            return jsonify({
                'success': False,
                'error': 'Échec de la mise à jour'
            }), 500
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @staticmethod
    def delete_user(user_id):
        """Supprimer un utilisateur"""
        try:
            if User.delete(user_id):
                return jsonify({
                    'success': True,
                    'message': 'Utilisateur supprimé avec succès'
                }), 200
            
            return jsonify({
                'success': False,
                'error': 'Utilisateur non trouvé'
            }), 404
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500