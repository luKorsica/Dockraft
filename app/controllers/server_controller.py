from flask import jsonify, request
from app.models.server import Server

class ServerController:
    
    @staticmethod
    def get_all_files():
        """Récupérer tous les utilisateurs"""
        try:
            servers = Server.find_all()
            return jsonify({
                'success': True,
                'data': servers,
                'count': len(servers)
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    

    @staticmethod
    def get_files(version="*",one='*', two="*", three="*"):
        """Récupérer tous les utilisateurs"""
        try:
            servers = Server.find_by_version(version,one, two, three)
            return jsonify({
                'success': True,
                'data': servers,
                'count': len(servers)
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
        

    
    @staticmethod
    def get_server(id):
        """Récupérer tous les utilisateurs"""
        try:
            servers = Server.find_server_by_id(id)
            return jsonify({
                'success': True,
                'data': servers,
                'count': len(servers)
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
        

    @staticmethod
    def create_server():
        """Créer un nouveau serveur"""
        try:
            data = request.get_json()
            
            
            server = Server.create(data)
            return jsonify({
                'success': True,
                'data': server,
                'message': 'Serveur créé avec succès'
            }), 201
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
        

    @staticmethod
    def start_server(id):
        """Démarrer le serveur"""
        try:
            data = request.get_json()
            
            
            server = Server.start_server(id)
            return jsonify({
                'success': True,
                'data': server,
                'message': 'Serveur démarrer avec succès'
            }), 201
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
        
    @staticmethod
    def playbook_server(id):
        """Demarrer le serveur"""
        try:
            data = request.get_json()
            
            
            server = Server.playbook_server(id, data)
            return jsonify({
                'success': True,
                'data': server,
                'message': 'Script executer avec succès'
            }), 201
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
