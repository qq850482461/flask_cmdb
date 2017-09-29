from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,current_user
from flask_principal import Principal, Permission, RoleNeed, identity_loaded,UserNeed
#,IdentityContext # 权限认证

# 初始化对象
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'  # 让session功能更加强壮
login_manager.login_view = 'auth.login'  # 制定系统默认的登录页面
login_manager.login_message = "请登录后再进行访问该页面！"

principals = Principal()
admin_permission = Permission(RoleNeed('admin'))


# 工厂化
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.conf')

    db.init_app(app)
    login_manager.init_app(app)
    principals.init_app(app)

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        #设置当前用户身份为login登录对象
        identity.user = current_user

        #添加UserNeed到identity user对象
        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        #每个Role添加到identity user对象，roles是User的多对多关联
        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role.name))


    # 注册蓝图
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .property import property as property_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(property_blueprint)

    return app
