from . import property
from flask import render_template
from ..models import Ip_Category
from flask_login import login_required


# 登记管理
@property.route('/record', methods=['GET', 'POST'])
@login_required
def record():
    return render_template('record.html')


# ip地址池分配管理
@property.route('/ip_address', methods=['GET', 'POST'])
@login_required
def ip():
    ip_category = Ip_Category.query.all()
    return render_template('ip_address.html', ip=ip_category)

