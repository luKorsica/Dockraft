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
    