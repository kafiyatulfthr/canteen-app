from flask import Flask
from flask_migrate import Migrate

from config import DevelopmentConfig

from flask_sqlalchemy import SQLAlchemy

# create an instance of the extension with initializing it
db = SQLAlchemy()

# instance of migrate flask
migrate = Migrate()

def app_kantins(config=DevelopmentConfig):
  app = Flask(__name__)
  app.config.from_object(config)
  
  # initialize extension instances
  db.init_app(app)
  db.app = app
  
  # migrate initialization
  migrate.init_app(app, db)
  migrate.app = app
  
    
  # ----------register blueprints of applications-----------
  
  # SUPLIER
  from app_kantins.entry.menu import app_menu as menu
  app.register_blueprint(menu)

  from app_kantins.process.ratings import app_ratings as ratings
  app.register_blueprint(ratings)

  from app_kantins.exit.reports import app_reports as reports
  app.register_blueprint(reports)

  return app 