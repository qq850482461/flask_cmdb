# roles路由的API接口函数
from . import auth
from flask import jsonify, request
from flask_login import login_required
from .. import db
from ..models import Role


# roles角色管理接口
@auth.route('/api/roles/query', methods=['GET'])
def roles_query():
    role_data = []
    res = {
        'code': 0,
        'msg': "",
        'count': 10,
        'data': []
    }
    try:
        role = Role.query.all()
    except Exception as e:
        res['msg'] = repr(e)
        res['count'] = 0
        return jsonify(res)
    else:
        if role is not None:
            for i in role:
                y = {
                    'id': i.id,
                    'user': i.name,
                    'text': i.description
                }
                role_data.append(y)

            res['data'] = role_data
            res['msg'] = 'success'
            res['count'] = len(role)
            return jsonify(res)


# roles增加修改管理接口
@auth.route('/api/roles/edit', methods=['POST'])
@login_required
def roles_edit():
    id = request.values.get('id')
    user = request.values.get('user')
    description = request.values.get('description')

    res = {'message': "succeed"}
    # 根据ID新增
    if id is not None and int(id) == 0:
        try:
            role = Role.query.get(int(id))
        except Exception as e:
            res['message'] = repr(e)
            return jsonify(res)
        else:
            new_role = Role(name=user, description=description)
            db.session.add(new_role)
            db.session.commit()
            return jsonify(res)
    # 根据ID修改
    elif id is not None and int(id) > 0:
        try:
            role = Role.query.get(int(id))
        except Exception as e:
            res['message'] = repr(e)
            return jsonify(res)
        else:
            role.name = user
            role.description = description
            db.session.commit()
            return jsonify(res)
    else:
        res['message'] = "Cannot find id"
        return jsonify(res)


# roles删除接口
@auth.route('/api/roles/delete', methods=['POST'])
@login_required
def roles_delete():
    id = request.values.get('id')
    res = {'message': "succeed"}

    if id is not None:
        try:
            role = Role.query.get(int(id))
            db.session.delete(role)
            db.session.commit()
            return jsonify(res)
        except Exception as e:
            res['message'] = repr(e)
            return jsonify(res)
    else:
        res['message'] = "Cannot find id"
        return jsonify(res)
