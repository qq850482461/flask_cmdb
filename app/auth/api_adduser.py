# 增加用户API接口
from . import auth
from flask import jsonify, request
from flask_login import login_required
from .. import db
from ..models import User, Role


# addusers查询角色接口
@auth.route('/api/user/query', methods=['GET'])
def userss_query():
    users_data = []
    res = {
        'code': 0,
        'msg': "",
        'count': 10,
        'data': []
    }
    try:
        user = User.query.all()

    except Exception as e:
        res['msg'] = repr(e)
        res['count'] = 0
        return jsonify(res)
    else:
        for i in user:
            str_time = i.created_time.strftime('%Y-%m-%d %H:%M:%S')
            role = i.roles
            if role:
                str_role = role[0].name
            else:
                str_role = ''
            y = {
                'id': i.id,
                'user': i.username,
                'time': str_time,
                'role': str_role
            }
            users_data.append(y)
        res['data'] = users_data
        res['msg'] = 'success'
        res['count'] = len(user)
        return jsonify(res)


# 新增和修改api接口
@auth.route('/api/edit_user', methods=['POST'])
@login_required
def edit_user():
    user_id = int(request.form['id'])
    user = request.form['user']
    pwd = request.form['pwd']
    select_role = request.form['select_role']
    res = {'status': 'success'}
    role = Role.query.filter_by(name=str(select_role)).first()

    if user_id == 0:
        try:
            new_user = User.query.filter_by(username=str(user)).first()
        except Exception as e:
            return jsonify({'status': repr(e)})
        else:
            if new_user is None and user_id == 0:
                new_user = User(username=user, password=pwd)
                new_user.roles = [role]
                db.session.add(new_user)
                db.session.commit()
                return jsonify(res)
            else:
                return jsonify({'status': 'repeat'})
    elif user_id != 0:
        try:
            old_user = User.query.get(user_id)
        except Exception as e:
            return jsonify({'status': repr(e)})
        else:
            if old_user is not None:
                old_user.username = user
                old_user.password = pwd
                old_user.roles.clear()
                old_user.roles = [role]
                db.session.commit()
                return jsonify(res)


# 用户名重复查询接口
@auth.route('/api/repeat_user', methods=['GET'])
def repeat_user():
    user = request.values.get('user')
    try:
        old_user = User.query.filter_by(username=str(user)).first()
    except Exception as e:
        return jsonify({'status': repr(e)})
    else:
        if old_user is None:
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'repeat'})


# roles删除接口
@auth.route('/api/user/delete', methods=['POST'])
@login_required
def users_delete():
    user_id = request.values.get('id')
    res = {'status': "succee"}

    try:
        user = User.query.get(int(user_id))
        user.roles.clear()
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        res['status'] = repr(e)
        return jsonify(res)
    else:
        return jsonify(res)
