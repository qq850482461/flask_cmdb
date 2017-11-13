#  email路由的API接口函数
from . import main
from flask import jsonify, request
from flask_login import login_required
from .. import db
from ..models import Email, Emailserver


# 邮箱查询接口
@main.route('/api/email/query', methods=['GET', 'POST'])
@login_required
def query_email():
    rep = {"data": None}
    all_servers = Emailserver.query.all()
    email_server = {}
    demo = {"id": None, "email": None, "password": None, "description": None, "pop": None,
            "pop_port": None, "smtp": None, "smtp_port": None}
    # 获得对应的字典
    for i in all_servers:
        email_server[i.name] = i.email
    # 前端传来select的值，进行分类
    if request.method == 'POST':
        value = request.form['type']
        if value == 'all':
            rep["data"] = demo
            return jsonify(rep)
        elif value in email_server:
            data = []
            # 转换json对象
            for i in list(email_server[value]):
                y = i.email_servers
                x = {
                    "id": i.id,
                    "email": i.email,
                    "password": i.password,
                    "description": i.description,
                    "pop": y.pop,
                    "pop_port": y.pop_port,
                    "smtp": y.smtp,
                    "smtp_port": y.smtp_port}
                data.append(x)
            rep['data'] = data
            return jsonify(rep)
        else:
            return jsonify(rep)


# 邮箱增加修改接口
@main.route('/api/email/add', methods=['GET', 'POST'])
@login_required
def add_email():
    if request.method == "POST":
        # 获取邮箱分类
        email_server = request.form['select_email']
        id = request.form['id']
        server = Emailserver.query.filter_by(name=email_server).first()
        # 新增
        if id == '0' and server is not None:
            email = Email(email=request.form['email'],
                          password=request.form['password'],
                          description=request.form['description']
                          )
            # 关联邮箱分类
            email.emailserver_id = server.id

            db.session.add(email)
            db.session.commit()
            return jsonify({"status": "success"})
        # 修改
        elif id != '0' and server is not None:
            email = Email.query.get(int(id))
            # 更新
            email.email = request.form['email']
            email.password = request.form['password']
            email.description = request.form['description']
            email.emailserver_id = server.id

            db.session.add(email)
            db.session.commit()
            return jsonify({"status": "success"})
        else:
            return jsonify({"status": "failed"})


# 邮箱删除改接口
@main.route('/api/email/delete', methods=['POST'])
@login_required
def delete_email():
    if request.method == 'POST':
        id = request.form['id']
        email = Email.query.get(id)
        if id and email is not None:
            db.session.delete(email)
            db.session.commit()
            return jsonify({"status": "success"})
        else:
            return jsonify({"status": "failed"})
