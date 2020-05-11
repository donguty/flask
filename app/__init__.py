from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
Bootstrap(app)
csrf = CSRFProtect(app)

from .views import page

def create_app(config):
  app.config.from_object(config)
  app.register_blueprint(page)
  csrf.init_app(app)
  
  return app
