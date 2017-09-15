from . import property
from flask import render_template, jsonify, request
from .. import db, admin_permission
from flask_login import login_required


# ip地址池分配管理
@property.route('/ip_address', methods=['GET', 'POST'])
@login_required
def ip():
    return render_template('ip_address.html')
