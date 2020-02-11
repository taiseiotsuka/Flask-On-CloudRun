from flask import Flask
from pathlib import Path

app = Flask(__name__, instance_path='%s/instance/' % Path.cwd())

from flaskr.example import example
from flaskr.actor import actor

app.register_blueprint(example)
app.register_blueprint(actor)