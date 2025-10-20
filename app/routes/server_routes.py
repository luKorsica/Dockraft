from flask import Blueprint
from app.controllers.server_controller import ServerController

server_bp = Blueprint('servers', __name__)

# Routes CRUD
server_bp.route('/servers', methods=['GET'])(ServerController.get_all_files)
