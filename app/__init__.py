from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


from .views import page

def create_app(config):
  app.config.from_object(config)
  app.register_blueprint(page)

  return app
