from . import db, login_manager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

# 用户<-->角色，多对多关联表
roles_users = db.Table(
    'user_role',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)

# 角色<-->节点,多对多关联表
roles_nodes = db.Table(
    'role_node',
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')),
    db.Column('node_id', db.Integer(), db.ForeignKey('node.id'))
)


# 用户表
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255))
    created_time = db.Column(db.DateTime, default=datetime.utcnow)
    roles = db.relationship('Role', secondary='user_role', backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return "<User_id:{0}>".format(self.id)

    # 这个方法是用于用户登录后返回数据库的ID到session中用来登录
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @property
    def password(self):
        raise AttributeError("密码不允许读取,请使用check_password_hash()进行验证密码")

    # 转换密码为hash存入数据库
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 检查密码
    def check_password_hash(self, password):
        return check_password_hash(self.password_hash, password)


# 角色表
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(80))
    # 多对多关联节点
    nodes = db.relationship('Node', secondary='role_node', backref=db.backref('roles', lazy='dynamic'))

    def __repr__(self):
        return "<Role_id:{0}>".format(self.id)


# 权限节点表
class Node(db.Model):
    __tablename__ = 'node'
    id = db.Column(db.Integer(), primary_key=True)
    parent_id = db.Column(db.Integer())
    url = db.Column(db.String(80))
    label = db.Column(db.String(80))
    icon = db.Column(db.String(80))
    order = db.Column(db.Integer())

    def __repr__(self):
        return "<Node_id:{0}>".format(self.id)


# 邮箱服务器分类
class Emailserver(db.Model):
    __tablename__ = 'email_server'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80))
    pop = db.Column(db.String(80))
    pop_port = db.Column(db.Integer())
    smtp = db.Column(db.String(80))
    smtp_port = db.Column(db.Integer())
    email = db.relationship('Email', backref='email_servers', lazy='dynamic')

    def __repr__(self):
        return "<Emailserver:{0}>".format(self.id)


# 邮箱存放表
class Email(db.Model):
    __tablename__ = 'email'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))
    description = db.Column(db.String(80))
    created_time = db.Column(db.DateTime, default=datetime.utcnow)
    emailserver_id = db.Column(db.Integer, db.ForeignKey('email_server.id'))

    def __repr__(self):
        return "<Email_id:{0}>".format(self.id)


# 邮箱运营商存放表
class EmailDomain(db.Model):
    __tablename__ = 'email_supplier'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(80))
    web = db.Column(db.String(80))
    operator = db.Column(db.String(80))
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    created_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<email_supplier_id:{0}>".format(self.id)


# IP分类,一对多
class Ip_Category(db.Model):
    __tablename__ = 'ip_category'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80))
    created_time = db.Column(db.DateTime, default=datetime.utcnow)
    ip_address = db.relationship('Ip_Addres', backref='ip_categorys', lazy='dynamic')

    def __repr__(self):
        return "<ip_class:{0}>".format(self.id)


# IP地址
class Ip_Addres(db.Model):
    __tablename__ = 'ip_address'
    id = db.Column(db.Integer(), primary_key=True)
    ip = db.Column(db.String(80))
    mac = db.Column(db.String(80))
    hostname = db.Column(db.String(80))
    enable = db.Column(db.Boolean(), default=True)
    created_time = db.Column(db.DateTime, default=datetime.utcnow)
    ip_category = db.Column(db.Integer, db.ForeignKey('ip_category.id'))

    def __repr__(self):
        return "<ip_address:{0}>".format(self.id)
