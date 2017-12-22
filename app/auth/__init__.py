from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
from . import api_menu
from . import api_roles
from . import api_adduser
