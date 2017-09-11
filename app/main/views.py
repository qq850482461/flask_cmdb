from . import main
from flask import render_template, redirect, jsonify, request
from flask_login import login_required
from .. import db, admin_permission
from ..models import Email, Emailserver, EmailDomain


# 自己定义一个错误页面传入错误代码,如果不是蓝图就是用errorhandler
@main.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='404'), 404


@main.app_errorhandler(403)
def page_not_found(error):
    return render_template('403.html', title='403'), 403


# 主页
@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html', name="test")


# 邮箱运营商web页面,增加修改运营商页面
@main.route('/email_web', methods=['GET', 'POST'])
@login_required
@admin_permission.require(http_exception=403)
def email_web():
    if request.method == "POST":

        id = request.form['id']
        #新增
        if id == '0':
            account = EmailDomain(
                email=request.form['email'],
                operator=request.form['operator'],
                username=request.form['username'],
                password=request.form['password'],
            )
            db.session.add(account)
            db.session.commit()
            return jsonify({"status": "success"})
        # 修改
        elif id != '0':
            account = EmailDomain.query.get(int(id))
            account.email = request.form['email']
            account.operator = request.form['operator']
            account.username = request.form['username']
            account.password = request.form['password']

            db.session.add(account)
            db.session.commit()

            return jsonify({"status": "success"})
        else:
            return jsonify({"status": "failed"})

    return render_template('email_web.html')


# 邮箱运营商管查询表单查询接口
@main.route('/api/email_web/query', methods=['GET'])
@login_required
def query_email_web():
    rep = {"code": 0, "msg": "success", "count": 1000, "count": []}
    data = []
    domain = EmailDomain.query.all()
    for i in domain:
        x = {
            'id': i.id,
            'email': i.email,
            'operator': i.operator,
            'username': i.username,
            'password': i.password,
            'created': i.created
        }
        data.append(x)
    rep['data'] = data
    return jsonify(rep)


# 邮箱运营商管理帐号密码,删除接口
@main.route('/api/email_web/delete', methods=['GET', 'POST'])
@login_required
def delete_email_web():
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


# 邮箱服务器管理页面
@main.route('/email_edit', methods=['GET', 'POST'])
@login_required
@admin_permission.require(http_exception=403)
def email_edit():
    return render_template('email_server.html')


# 获取邮箱服务器和删除服务器API接口
@main.route('/api/email_server', methods=['GET', 'POST'])
@login_required
def email_server():
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


# 邮箱查询页面
@main.route('/email', methods=['GET', 'POST'])
@login_required
def email():
    email_server = Emailserver.query.all()
    return render_template('email.html', email_server=email_server)


# 邮箱查询接口
@main.route('/api/queryemail', methods=['GET', 'POST'])
@login_required
def queryemail():
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
                y = i.email_server
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
@main.route('/api/add_email', methods=['GET', 'POST'])
@login_required
def add_email():
    if request.method == "POST":
        email_server = request.form['select_email']
        id = request.form['id']
        print(id)
        server = Emailserver.query.filter_by(name=email_server).first()
        # 新增
        if id == '0' and server is not None:
            email = Email(email=request.form['email'], password=request.form['password'],
                          description=request.form['description'])
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
        if id and email_server is not None:
            db.session.delete(email)
            db.session.commit()
            return jsonify({"status": "success"})
        else:
            return jsonify({"status": "failed"})
