from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#初始化对象
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'#制定系统默认的登录页面

#工厂化
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.conf')

    db.init_app(app)
    login_manager.init_app(app)

    # 注册蓝图
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app
