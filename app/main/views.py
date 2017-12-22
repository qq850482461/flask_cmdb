# 通用视图函数
from . import main
from flask import render_template, redirect, jsonify, request, abort, g, session
from flask_login import login_required, current_user
from .. import db, permission
from ..models import Email, Emailserver, EmailDomain, Node
from datetime import datetime
from operator import attrgetter


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
@permission
def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', name=user_agent,test='index:fuck')


# 邮箱运营商web页面,增加修改运营商页面
@main.route('/email_support/', methods=['GET', 'POST'])
@login_required
@permission
def email_support():
    if request.method == "POST":
        id = request.form['id']
        # 新增
        if id == '0':
            account = EmailDomain(
                email=request.form['email'],
                operator=request.form['operator'],
                web=request.form['web'],
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
            account.web = request.form['web']
            account.username = request.form['username']
            account.password = request.form['password']
            db.session.add(account)
            db.session.commit()

            return jsonify({"status": "success"})
        else:
            return jsonify({"status": "failed"})

    return render_template('email_support.html')


# 邮箱服务器管理页面
@main.route('/email_server/', methods=['GET', 'POST'])
@login_required
@permission
def email_server():
    return render_template('email_server.html')


# 邮箱查询页面
@main.route('/email/', methods=['GET', 'POST'])
@login_required
@permission
def email():
    email_server = Emailserver.query.all()
    return render_template('email.html', email_server=email_server)
