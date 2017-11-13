# email_web路由的API接口函数
from . import main
from flask import jsonify, request
from flask_login import login_required
from .. import db
from ..models import EmailDomain


# 邮箱运营商管查询表单查询接口
@main.route('/api/email_support/query', methods=['GET'])
@login_required
def query_email_support():
    rep = {"code": 0, "msg": "success", "count": 1000, "data": []}
    data = []
    domain = EmailDomain.query.all()
    for i in domain:
        x = {
            'id': i.id,
            'email': i.email,
            'operator': i.operator,
            'web': i.web,
            'username': i.username,
            'password': i.password,
            'created': i.created_time
        }
        data.append(x)
    rep['data'] = data
    return jsonify(rep)


# 邮箱运营商管理帐号密码,删除接口
@main.route('/api/email_support/delete', methods=['POST'])
@login_required
def delete_email_support():
    if request.method == 'POST':
        value = request.form.getlist('id')
        if value is not None:
            for i in value:
                account = EmailDomain.query.get(int(i))
                db.session.delete(account)
                db.session.commit()
            return jsonify({"status": "success"})
        else:
            return jsonify({"status": "failed"})
