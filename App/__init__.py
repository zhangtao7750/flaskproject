from flask import  Flask
from App.views import init_view
# from App.models import init_model
from App.ext import init_ext
from App.settings import envs

def create_app():
    app=Flask(__name__)
    # app.register_blueprint(blue)
    #数据库+驱动：//用户名：密码@主机：端口
    # app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///slqite.db"
    # app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:Zt@647409@localhost:3306/myflask"
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config.from_object(envs.get("develop"))
    # init_model(app)
    init_view(app)
    init_ext(app)
    return app