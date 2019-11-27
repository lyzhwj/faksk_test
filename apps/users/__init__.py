from flask import Blueprint

users_bp = Blueprint('users', __name__, url_prefix='/index')

from apps.users import view
