from flask_script import Manager, Shell
from app import create_app, db
from app.models import *  # 一定要引入模型类
from flask_migrate import Migrate, MigrateCommand  # flask 迁移数据

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# 创建数据库
@manager.command
def create_db():
    db.create_all()


if __name__ == '__main__':
    app.run()
    #manager.run()
