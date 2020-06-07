
#
# from flask_sqlalchemy import SQLAlchemy
# models=SQLAlchemy()
# def init_model(app):
#     models.init_app(app)

from App.ext import models
class User(models.Model):
    id=models.Column(models.Integer,primary_key=True)
    username=models.Column(models.String(50))

    def save(self):
        models.session.add(self)
        models.session.commit()