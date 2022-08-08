from flask import Blueprint
from controllers.AuthorController import list,create,delete

author_bp = Blueprint('author_bp', __name__)
author_bp.route('/list', methods=['GET', 'POST'])(list)
author_bp.route('/create', methods=['POST'])(create)
author_bp.route('/delete/<name>', methods=['DELETE'])(delete)

