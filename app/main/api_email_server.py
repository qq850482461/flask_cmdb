# email_server路由的API接口函数
from . import main
from flask import jsonify, request
from flask_login import login_required
from .. import db
from ..models import Emailserver


# emailserver路由查询接口和新增修改接口
@main.route('/api/email_server/query', methods=['GET', 'POST'])
@login_required
def query_server():
    # 查询所有datatables
    datatables = {"data": None}
    query = []
    if request.method == "GET":
        emailserver = Emailserver.query.all()
        for i in emailserver:
            value = {
                "id": i.id,
                "email": i.name,
                "pop": i.pop,
                "pop_port": i.pop_port,
                "smtp": i.smtp,
                "smtp_port": i.smtp_port}
            query.append(value)
        datatables["data"] = query
        return jsonify(datatables)
    # 新增datatables
    if request.method == 'POST':
        email = request.form['email']
        id = request.form['id']
        # 根据ID判断是新增还是修改
        if email is not None and id == '0':
            email_server = Emailserver(name=email,
                                       pop=request.form['pop_server'],
                                       pop_port=request.form['pop_port'],
                                       smtp=request.form['smtp_server'],
                                       smtp_port=request.form['smtp_port'])
            db.session.add(email_server)
            db.session.commit()
            return jsonify({"status": "success"})
        elif id != '0':
            # update方法需要是basequery对象
            email_server = Emailserver.query.filter_by(id=int(id))
            email_server.update(
                {'name': request.form['email'],
                 'pop': request.form['pop_server'],
                 'pop_port': request.form['pop_port'],
                 'smtp': request.form['smtp_server'],
                 'smtp_port': request.form['smtp_port']})
            db.session.commit()
            return jsonify({"status": "success"})
        else:
            return jsonify({"status": "failed"})


# 删除emailserver的接口
@main.route('/api/email_server/delete', methods=['POST'])
@login_required
def delete_email_server():
    if request.method == 'POST':
        id = request.form['id']
        email_server = Emailserver.query.get(id)
        if id and email_server is not None:
            db.session.delete(email_server)
            db.session.commit()
            return jsonify({"status": "success"})
        else:
            return jsonify({"status": "failed"})
