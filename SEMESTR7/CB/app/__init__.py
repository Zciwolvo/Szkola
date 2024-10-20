from flask import Blueprint

cb = Blueprint('cb', __name__, template_folder='templates', static_folder='static')

from . import index
