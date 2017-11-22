# menu路由的api接口
from . import auth
from .. import db
from ..models import Node, Role
from flask import request, jsonify
from flask_login import login_required


# 菜单管理API查询接口
@auth.route('/api/menu/query', methods=['GET'])
@login_required
def query_node():
    role_id = request.args.get("id")
    try:
        # 角色关联节点列表
        if role_id is not None:
            role = Role.query.get(int(role_id))
            node_list = [i.id for i in role.nodes]
        else:
            node_list = []
        # 父节点和子节点列表
        p_lists = Node.query.filter_by(parent_id=0).order_by(Node.order).all()
        c_lists = Node.query.filter(Node.parent_id != 0).order_by(Node.order).all()
    except Exception as e:
        print(e)
        return jsonify({'message': 'failed'})
    else:
        req = []
        for i in (p_lists + c_lists):
            y = {
                "id": i.id,
                "pId": i.parent_id,
                "name": i.label,
                "url": i.url,
                "order": i.order,
                "ico": i.icon
            }
            # 判断是否关联
            if i.id in node_list:
                y["checked"] = True

            # 判断是否为父ID
            if i.parent_id == 0:
                y["childOuter"] = False
                y["open"] = True
            req.append(y)
        return jsonify(req)


# 菜单管理API删除接口
@auth.route('/api/menu/delete', methods=['POST'])
@login_required
def menu_delete():
    id = request.values.get('id')
    res = {'message': "succeed"}
    if id is not None:
        node = Node.query.get(int(id))
        try:
            db.session.delete(node)
            db.session.commit()
            return jsonify(res)
        except Exception as e:
            res['message'] = e.__repr__()
            return jsonify(res)


# 菜单管理修改_新增API接口
@auth.route('/api/menu/add', methods=['POST'])
@login_required
def menu_add():
    id = int(request.values.get('id'))
    node = Node.query.get(int(id))
    res = {'status': 200, 'message': "succeed"}
    # 修改内容
    if id != 0 and node is not None:
        node.parent_id = request.values.get('pId')
        node.url = request.values.get('url')
        node.label = request.values.get('label')
        node.order = request.form['order']
        node.icon = request.values.get('ico')
        try:
            db.session.commit()
            return jsonify(res)
        except Exception as e:
            db.session.rollback()
            res['message'] = e.__repr__()
            return jsonify(res)
    # 新增
    elif id == 0:
        order = request.form['order']
        node = Node(order=order, label="新节点", parent_id=0)
        try:
            db.session.add(node)
            db.session.commit()
            return jsonify(res)
        except Exception as e:
            db.session.rollback()
            res['message'] = e.__repr__()
            return jsonify(res)
    else:
        res['message'] = 'failed'
        return jsonify(res)


# 菜单排序API接口
@auth.route('/api/menu/order', methods=['POST'])
@login_required
def order():
    data = request.get_json()
    res = {'message': "succeed"}
    if data is not None:
        for i in data:
            id = i["id"]
            order = i["order"]
            try:
                node = Node.query.get(int(id))
                node.order = int(order)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                res['message'] = e.__repr__()
                return jsonify(res)
        return jsonify(res)


# 角色关联菜单API接口
@auth.route('/api/menu/relational', methods=['POST'])
@login_required
def relational():
    data = request.get_json()
    # print(data)
    res = {'message': "succeed"}
    if data is not None:
        role_id = data['role_id']
        # 选中列表 index是字典类型
        selecd = data['selecd']
        # 是否为空 返回为boolean值
        empty = data['empty']

        try:
            role = Role.query.get(role_id)
            selecd_list = [Node.query.get(i["id"]) for i in selecd]
        except Exception as e:
            db.session.rollback()
            res['message'] = repr(e)
            return jsonify(res)
        else:
            # 多对多关联列表
            role_node = role.nodes
            if empty is True:
                # clear直接清除所有的关联对象
                role_node.clear()
                db.session.commit()
                return jsonify(res)
            else:
                role_node.clear()
                for i in selecd_list:
                    role_node.append(i)
                db.session.commit()
                return jsonify(res)
    else:
        res['message'] = "Data is None!"
        return jsonify(res)
