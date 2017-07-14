from . import db
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash#转换密码用到的库
from flask_security import RoleMixin, UserMixin#登录和角色需要继承的对象

# #角色<-->用户，关联表
# roles_users = db.Table(
#     'roles_users',
#     db.Column('user_id',db.Integer(),db.ForeignKey('users.id')),
#     db.Column('role_id',db.Integer(),db.ForeignKey('roles.id'))
# )
#
#
# #角色表
# class Role(db.Model,RoleMixin):
#     __tablename__ = 'role'
#     id = db.Column(db.Integer(),primary_key=True)
#     name = db.Column(db.String(80),unique=True)
#
#     def __repr__(self):
#         return "<Role_id:{0}>".format(self.id)
#
#
# #用户表
# class User(db.Model,UserMixin):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer(),primary_key=True)
#     username = db.Column(db.String(80),unique=True,nullable=False)
#     password = db.Column(db.String(80,nullable=False))
#     #多对多关联
#     roles = db.relationship('Role',secondary='roles_users',backref=db.backref('users',lazy='dynamic'))
#
#
#     def __repr__(self):
#         return "<User_id:{0}>".format(self.id)
#
#     @property
#     def password(self):
#         raise AttributeError("密码不允许读取")
#
#     #转换密码为hash存入数据库
#     @password.setter
#     def password(self,password):
#         self.password = generate_password_hash(password)
#
#     #检查密码
#     def check_password_hash(self, password):
#         return check_password_hash(self.password,password)
#
#

class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer(), primary_key=True)
    test = db.Column(db.String(80))

