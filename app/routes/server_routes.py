from flask import Blueprint
from app.controllers.server_controller import ServerController

server_bp = Blueprint('servers', __name__)

# Routes CRUD
server_bp.route('/images', methods=['GET'])(ServerController.get_all_files)
server_bp.route('/images/<version>', methods=['GET'])(ServerController.get_files)
server_bp.route('/images/<version>/<one>', methods=['GET'])(ServerController.get_files)
server_bp.route('/images/<version>/<one>/<two>', methods=['GET'])(ServerController.get_files)
server_bp.route('/images/<version>/<one>/<two>/<three>', methods=['GET'])(ServerController.get_files)


# Routes CRUD
server_bp.route('/servers', methods=['GET'])(ServerController.get_all_files)
server_bp.route('/servers/<id>', methods=['GET'])(ServerController.get_server)
server_bp.route('/servers/<id>', methods=['PUT'])(ServerController.start_server)
server_bp.route('/servers/action/<id>', methods=['POST'])(ServerController.playbook_server)
server_bp.route('/servers', methods=['POST'])(ServerController.create_server)

