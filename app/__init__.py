from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#初始化对象
db = SQLAlchemy()

#工厂化
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.conf')
    db.init_app(app)

    # 注册蓝图
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app
