from . import property
from flask import render_template, jsonify, request
from .. import db, admin_permission
from ..models import Ip_Addres, Ip_Category
from flask_login import login_required
from IPy import IP


# ip地址池分配管理
@property.route('/ip_address', methods=['GET', 'POST'])
@login_required
def ip():
    ip_category = Ip_Category.query.all()
    return render_template('ip_address.html', ip=ip_category)


# ip地址池删除接口
@property.route('/api/ip_address/delete', methods=['POST'])
@login_required
def delete():
    id_list = request.form.getlist('id')
    if request.method == 'POST':
        if id_list is not None:
            for i in id_list:
                ip_addres = Ip_Addres.query.get(int(i))
                db.session.delete(ip_addres)
                db.session.commit()
            return jsonify({"status": "success"})
        else:
            return jsonify({"status": "failed"})


# ip地址池增加接口
@property.route('/api/ip_address/add', methods=['POST'])
@login_required
def add_ip():
    ip_address = request.form['ip_address']
    subnet_mask = request.form['subnet_mask']
    select = request.form['select']
    ip_category = Ip_Category.query.filter_by(name=select).first()

    if ip_address and ip_address is not None:
        try:
            ip = IP(ip_address).make_net(subnet_mask)
        except:
            return jsonify({"status": "failed"})
        else:
            # 获取到IP网络段转换为Str写入数据库
            for i in ip:
                str_ip = str(i)
                ip_address = Ip_Addres(ip=str_ip, ip_category=ip_category.id)
                db.session.add(ip_address)
                db.session.commit()
            return jsonify({"status": "success"})


# IP地址查询接口,返回json数据
@property.route('/api/ip_address/query', methods=['GET'])
@login_required
def query_ip():
    page = request.args['page']
    limit = request.args['limit']
    select = request.args['select']
    search = request.values.get('search')
    print(search)
    rep = {
        "code": 0,
        "msg": "success",
        "count": 0,
        "data": []
    }
    data = []

    # ip分类的select的value列表
    ip_category = [i.name for i in Ip_Category.query.all()]

    # 根据select的分类返回json数据
    if select in ip_category:

        # 获取到IP分类获取到的ORM对象
        category = Ip_Category.query.filter_by(name=select).first()

        if search is not None:
            # 搜索结果
            paging_data = category.ip_address.filter_by(ip=search)
            # 通过搜索结果进行判断返回搜索结果
            if paging_data is not None:
                for i in paging_data:
                    value = {
                        'id': i.id,
                        'ip': i.ip,
                        'mac': i.mac,
                        'enable': i.enable,
                        'hostname': i.hostname
                    }
                    data.append(value)
                rep['data'] = data
                rep['count'] = paging_data.count()
                return jsonify(rep)
        else:
            # 根据limit page算出分页对象
            if int(page) != 1:
                paging_data = category.ip_address.limit(int(limit)).offset(int(limit) * (int(page) - 1))
            else:
                paging_data = category.ip_address.limit(int(limit))

            # 结果数量
            count = category.ip_address.count()

            for i in paging_data:
                value = {
                    'id': i.id,
                    'ip': i.ip,
                    'mac': i.mac,
                    'enable': i.enable,
                    'hostname': i.hostname
                }
                data.append(value)
            rep['count'] = count
            rep['data'] = data
            return jsonify(rep)
