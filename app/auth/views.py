from . import auth
from ..models import User
from flask import redirect,render_template,request,url_for,flash
from flask_login import login_user,logout_user

#登录
@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password_hash(password):
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash("账户或密码错误！")
    return render_template('login.html')

#注销
@auth.route('/logout',methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

#更改密码
@auth.route('/resetpw',methods=['GET','POST'])
def resetpw():
    if request.method == 'POST':
        oldpassword = request.form['oldpassword']
        newpassword = request.form['newpassword']
        print(oldpassword,newpassword)
    return render_template('resetpassword.html')