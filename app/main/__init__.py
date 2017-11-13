from flask import Blueprint

main = Blueprint('main', __name__)
from . import views
# api接口文件
from . import api_email_support
from . import api_email_server
from . import api_email
