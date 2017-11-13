from flask import Blueprint

property = Blueprint('property', __name__)
from . import views
from . import api_ip_address
