from . import auth
from .. import db, admin_permission
from ..models import User, Role
from flask import redirect, render_template, request, url_for, flash, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from flask_principal import Identity, AnonymousIdentity, identity_changed, current_app, IdentityContext


# 上下文
@auth.app_context_processor
def context():
    admin = IdentityContext(admin_permission)
    return dict(admin=admin)

# 登录
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        check = request.form.get('check')
        user = User.query.filter_by(username=username).first()
        if user is not None and user.check_password_hash(password):
            if check:
                login_user(user, remember=True)
            else:
                login_user(user)
            # 身份变化
            identity_changed.send(
                current_app._get_current_object(),
                identity=Identity(user.id))

            return redirect(url_for('main.index'))
        else:
            flash("账户或密码错误！")
    return render_template('login.html')


# 注销
@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    # 注销后身份变成匿名
    identity_changed.send(
        current_app._get_current_object(),
        identity=AnonymousIdentity())
    return redirect(url_for('auth.login'))


# 更改密码
@auth.route('/resetpw', methods=['GET', 'POST'])
@login_required
def resetpw():
    if request.method == 'POST':
        oldpassword = request.form['oldpassword']
        newpassword = request.form['newpassword']
        user = current_user
        if user is not None:
            if user.check_password_hash(oldpassword):
                user.password = newpassword
                db.session.commit()
                flash("密码修改成功跳转重新登录")
                logout_user()
                return redirect(url_for('auth.login'))
            else:
                flash("原密码错误")

    return render_template('resetpassword.html')


# 增加用户
@auth.route('/adduser', methods=['GET', 'POST'])
@login_required
@admin_permission.require(http_exception=403)
def adduser():
    all_users = User.query.order_by(User.id.desc())
    all_roles = Role.query.all()

    if request.method == 'POST':
        username = request.form['user']
        password = request.form['password']
        select = request.form.getlist('select')
        roles = []
        # 转换成为Role对象的list
        for i in select:
            role = Role.query.filter_by(name=i).first()
            roles.append(role)

        user = User.query.filter_by(username=username).first()
        res = {'status': 200, 'message': "succeed"}

        # 增加用户模块
        if username and password is not None:
            # 判断是否存在该用户
            if user is None:
                user = User(username=username, password=password)
                user.roles = roles
                db.session.add(user)
                db.session.commit()
                # 返回json到前端
                return jsonify(res)
            else:
                print("更新操作执行")
                user.username = username
                user.password = password
                user.roles = roles
                db.session.add(user)
                db.session.commit()
                return jsonify(res)

    return render_template('adduser.html', roles=all_roles, test=all_users)


# 查询api接口
@auth.route('/api/edit_user', methods=['POST'])
@login_required
@admin_permission.require(http_exception=403)
def edit_user():
    if request.method == 'POST':
        id = request.form['id']
        act = request.form['act']

        # 查询
        if act == "query":
            user = User.query.get(id)
            roles = []
            if user is not None:
                res = {"username": user.username, }
                for i in user.roles:
                    roles.append(i.name)
                res["roles"] = roles
            return jsonify(res)
        # 删除
        if act == "delect":
            user = User.query.get(id)
            db.session.delete(user)
            db.session.commit()
            res = {"message": 200}
            return jsonify(res)
