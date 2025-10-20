from flask import Blueprint
from app.controllers.server_controller import ServerController

server_bp = Blueprint('servers', __name__)

# Routes CRUD
server_bp.route('/servers', methods=['GET'])(ServerController.get_all_files)
server_bp.route('/servers/<version>', methods=['GET'])(ServerController.get_files)
server_bp.route('/servers/<version>/<one>', methods=['GET'])(ServerController.get_files)
server_bp.route('/servers/<version>/<one>/<two>', methods=['GET'])(ServerController.get_files)
server_bp.route('/servers/<version>/<one>/<two>/<three>', methods=['GET'])(ServerController.get_files)
server_bp.route('/servers', methods=['POST'])(ServerController.create_server)

