from flask import Flask
from flask_script import Manager
from App import create_app
import os
from flask_migrate import MigrateCommand
# envs=os.environ.get()

app = create_app()
manager=Manager(app=app)
manager.add_command("db",MigrateCommand)

if __name__ == '__main__':
    # app.run()
    manager.run()
