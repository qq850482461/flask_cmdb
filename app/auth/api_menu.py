# menu路由的api接口
from . import auth
from .. import db
from ..models import Node
from flask import request, jsonify
from flask_login import login_required


# 菜单管理API查询接口
@auth.route('/api/menu/query', methods=['GET'])
@login_required
def query_node():
    p_lists = Node.query.filter_by(parent_id=0).order_by(Node.order).all()
    c_lists = Node.query.filter(Node.parent_id != 0).order_by(Node.order).all()
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
