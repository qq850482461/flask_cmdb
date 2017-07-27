from . import main
from flask import render_template,redirect
from flask_login import login_required

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

