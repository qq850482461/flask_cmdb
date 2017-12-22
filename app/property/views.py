from . import property
from .. import permission
from flask import render_template
from ..models import Ip_Category
from flask_login import login_required


# ip地址池分配管理
@property.route('/ip_address', methods=['GET', 'POST'])
@login_required
@permission
def ip():
    ip_category = Ip_Category.query.all()
    return render_template('ip_address.html', ip=ip_category)
