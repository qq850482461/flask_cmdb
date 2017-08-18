from . import main
from flask import render_template,redirect,jsonify,request
from flask_login import login_required
from .. import db,admin_permission

# 自己定义一个错误页面传入错误代码,如果不是蓝图就是用errorhandler
@main.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='404'), 404

@main.app_errorhandler(403)
def page_not_found(error):
    return render_template('403.html', title='403'), 403

@main.route('/',methods=['GET','POST'])
@login_required
def index():
    return render_template('index.html',name="test")


@main.route('/email',methods=['GET','POST'])
@login_required
@admin_permission.require(http_exception=403)
def email():

    return render_template('email.html')

@main.route('/api/queryemail',methods=['GET','POST'])
@login_required
@admin_permission.require(http_exception=403)
def queryemail():
    rep = {"data": None}
    if request.method == 'POST':
        value = request.form['type']
        print(value)
        if value == "选项1":
            test = [{"id":'66', "email": "选项1@test.com", "password": "66","description":"TEST","pop":"POP","pop_port":995,"smtp":"SMTP","smtp_port":58},
                    {"id": '77', "email": "771@test.com", "password": "66", "description": "TEST", "pop": "POP","pop_port":57,
                     "smtp": "SMTP","smtp_port":58}]
            rep['data'] = test
            return jsonify(rep)
    test = [{"id":'7', "email": "fanny@tangdynastytours.com", "password": "Tdt2017..","description":"TEST","pop":"pop.fastmail.com","pop_port":995,"smtp":"smtp.fastmail.com","smtp_port":465},{"id":'6', "email": "test@test.com", "password": "66","description":"TEST","pop":"POP","pop_port":57,"smtp":"SMTP","smtp_port":58}]
    rep['data'] = test
    return jsonify(rep)