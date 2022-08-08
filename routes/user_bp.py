from flask import Blueprint
from controllers.UserController import list

user_bp = Blueprint('user_bp', __name__)
user_bp.route('/list', methods=['GET'])(list)
