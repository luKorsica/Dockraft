from flask import Blueprint
from app.controllers.user_controller import UserController

user_bp = Blueprint('users', __name__)

# Routes CRUD
user_bp.route('/users', methods=['GET'])(UserController.get_all_users)
user_bp.route('/users/<user_id>', methods=['GET'])(UserController.get_user)
user_bp.route('/users', methods=['POST'])(UserController.create_user)
user_bp.route('/users/<user_id>', methods=['PUT'])(UserController.update_user)
user_bp.route('/users/<user_id>', methods=['DELETE'])(UserController.delete_user)