from flask import Blueprint
from controllers.AuthController import login, register

auth_bp = Blueprint('auth_bp', __name__)
auth_bp.route('/login', methods=['GET','POST'])(login)
auth_bp.route('/register', methods=['GET', 'POST'])(register)

