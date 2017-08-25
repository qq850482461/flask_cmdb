from . import main
from flask import render_template, redirect, jsonify, request
from flask_login import login_required
from .. import db, admin_permission
from ..models import Email, Emailserver


# 自己定义一个错误页面传入错误代码,如果不是蓝图就是用errorhandler
@main.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='404'), 404


@main.app_errorhandler(403)
def page_not_found(error):
    return render_template('403.html', title='403'), 403


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html', name="test")


# 邮箱查询页面
@main.route('/email', methods=['GET', 'POST'])
@login_required
def email():
    return render_template('email.html')


# 邮箱服务器管理页面
@main.route('/email_edit', methods=['GET', 'POST'])
@login_required
def email_edit():
    datatables = {"data": None}
    query = []
    if request.method == "POST":
        if request.form['type'] == "query_emailserver":
            emailserver = Emailserver.query.all()
            for i in emailserver:
                value = {"id":i.id, "email":i.name,"pop":i.pop,"pop_port":i.pop_port,"smtp":i.smtp,"smtp_port":i.smtp_port}
                query.append(value)
            datatables["data"] = query
            return jsonify(datatables)
    return render_template('email_server.html')


# 邮箱查询接口
@main.route('/api/queryemail', methods=['GET', 'POST'])
@login_required
def queryemail():
    rep = {"data": None}
    if request.method == 'POST':
        value = request.form['type']
        print(value)
        if value == "选项1":
            test = [{"id": '66', "email": "选项1@test.com", "password": "66", "description": "TEST", "pop": "POP",
                     "pop_port": 995, "smtp": "SMTP", "smtp_port": 58},
                    {"id": '77', "email": "771@test.com", "password": "66", "description": "TEST", "pop": "POP",
                     "pop_port": 57,
                     "smtp": "SMTP", "smtp_port": 58}]
            rep['data'] = test
            return jsonify(rep)
    test = [{"id": '7', "email": "fanny@tangdynastytours.com", "password": "Tdt2017..", "description": "TEST",
             "pop": "pop.fastmail.com", "pop_port": 995, "smtp": "smtp.fastmail.com", "smtp_port": 465},
            {"id": '6', "email": "test@test.com", "password": "66", "description": "TEST", "pop": "POP", "pop_port": 57,
             "smtp": "SMTP", "smtp_port": 58}]
    rep['data'] = test
    return jsonify(rep)


# 邮箱服务器更新
@main.route('/api/queryemail_server', methods=['GET', 'POST'])
@login_required
def queryemail_server():
    rep = {"status": "success"}
    if request.method == 'POST':
        email = request.form['email']
        if email is not None:
            email_server = Emailserver(name=email, pop=request.form['pop_server'], pop_port=request.form['pop_port'],
                                       smtp=request.form['smtp_server'], smtp_port=request.form['smtp_port'])
            db.session.add(email_server)
            db.session.commit()
            return jsonify(rep)
        else:
            return jsonify({"status": "failed"})

