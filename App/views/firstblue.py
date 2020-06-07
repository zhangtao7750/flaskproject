from flask import Blueprint,render_template
from App.models import models,User
blue=Blueprint('blue',__name__)
@blue.route("/")
def index():
    # return 'this is __blueprint'
    return render_template('index.html',msg='我吃什么????')


@blue.route('/createdb/')
def createdb():
    models.create_all()
    return "创建成功"


@blue.route('/adduser/')
def add_user():
    user=User()
    user.username='synair'
    # models.session.add(user)
    # models.session.commit()
    user.save()
    return "news user succeed"

@blue.route('/dropdb/')
def dropdb():
    models.drop_all()

    return 'drop succeed'