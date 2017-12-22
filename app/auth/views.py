from . import auth
from .. import db,permission
from ..models import User, Role, Node
from flask import redirect, render_template, request, url_for, flash, jsonify, session, g
from flask_login import login_user, logout_user, current_user, login_required
from operator import attrgetter


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

            nodes = current_user.roles[0].nodes
            # 当前登录用户拥有的父菜单类
            parent_lists = [i for i in nodes if i.parent_id == 0]
            # 当前登录用户拥有的子菜单
            child_lists = [i for i in nodes if i.parent_id != 0]
            # 父菜单根据order排序
            parent_order = sorted(parent_lists, key=attrgetter("order"))
            # 最终传给jinja2前端的列表
            nodes_order = []
            # 序列化
            for i in parent_order:
                query = [child for child in child_lists if i.id == child.parent_id]
                # 有子菜单
                if query:
                    dic = {}
                    order = sorted(query, key=attrgetter("order"))
                    child_list_order = [{'name': i.label, 'url': i.url, 'icon': i.icon} for i in order]
                    name_icon = i.label + ':' + i.icon
                    dic[name_icon] = child_list_order
                    nodes_order.append(dic)
                else:
                    dic = {}
                    node = [{'name': i.label, 'url': i.url, 'icon': i.icon}]
                    dic['index'] = node
                    nodes_order.append(dic)
            # 传递到session
            session['menu'] = nodes_order
            return redirect(url_for('main.index'))
        else:
            flash("账户或密码错误！")
    return render_template('login.html', )


# 注销
@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


# 更改密码
@auth.route('/resetpw', methods=['GET', 'POST'])
@login_required
@permission
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


# 菜单管理
@auth.route('/menu', methods=['GET', 'POST'])
@login_required
@permission
def menu():
    return render_template('menu.html')


# 角色页面
@auth.route('/roles', methods=['GET', 'POST'])
@login_required
@permission
def role():
    return render_template('role.html')


# 增加用户
@auth.route('/adduser', methods=['GET', 'POST'])
@login_required
@permission
def adduser():
    all_roles = Role.query.all()
    return render_template('adduser.html', roles=all_roles)



