from flask import Flask

app = Flask(__name__, instance_relative_config=False)
app.config.from_pyfile('../instance/flask.cfg')

from . import views
