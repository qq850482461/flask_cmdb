from . import db,login_manager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash#转换密码用到的库
from flask_login import UserMixin

# from flask_security import RoleMixin,UserMixin#登录和角色需要继承的对象

#角色<-->用户，关联表
roles_users = db.Table(
    'role_user',
    db.Column('user_id',db.Integer(),db.ForeignKey('user.id')),
    db.Column('role_id',db.Integer(),db.ForeignKey('role.id'))
)


#角色表
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(80),unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return "<Role_id:{0}>".format(self.id)


#用户表
class User(db.Model,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    password_hash = db.Column(db.String(255))
    #多对多关联
    roles = db.relationship('Role',secondary='role_user',backref=db.backref('users',lazy='dynamic'))


    def __repr__(self):
        return "<User_id:{0}>".format(self.id)

    # 这个方法是用于用户登录后返回数据库的ID到session中用来登录
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    @property
    def password(self):
        raise AttributeError("密码不允许读取,请使用check_password_hash()进行验证密码")
        return


    #转换密码为hash存入数据库
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    #检查密码
    def check_password_hash(self, password):
        return check_password_hash(self.password_hash,password)





