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
    