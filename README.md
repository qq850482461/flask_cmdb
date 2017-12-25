# flask_cmdb
基于Flask的CMDB系统,功能比较简单主要根据目前公司的情况写的一个练手项目.
代码很烂,知道自己有很多不足,以后的学习应该要改进,
项目需要部署在gunicorn 或者 uwsgi上配合nginx启动.

### python版本:python3.6 
### 数据库: mysql5.6
## 步骤
1.安装requirements.txt 项目依赖包,建议使用虚拟环境安装.
> pip install -r requirements.txt

2.mysql数据库配置文件
[数据库配置文件](https://github.com/qq850482461/flask_cmdb/blob/master/app/config.conf)
> /app/config.conf

3.初始化数据库
创建一个项目数据库

1.创建数据库
> cteate database CMDB;

2.初始化项目ORM
> python manager.py create_db

3.导入数据结构
> mysql -uroot -p CMDB < cmdb.sql

4.启动项目
>python manager.py runserver --host 0.0.0.0 --port 9008
