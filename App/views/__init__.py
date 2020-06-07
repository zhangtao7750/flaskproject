# def init_route(app):
#     @app.route('/')
#     def hello_world():
#         return 'Hello World!'
#
#     @app.route('/hello/')
#     def hello():
#         return "this is hello"

from .firstblue import blue
from .secondblue import second
from .thirdblue import third
def init_view(app):
    app.register_blueprint(blue)
    app.register_blueprint(second)
    app.register_blueprint(third)