import os
import pymysql

# set the base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Create the super class
class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_COMMIT_ON_TEARDOWN = True
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  
  
# Create the development config
class DevelopmentConfig(Config):
  DEBUG = True
  # SQLALCHEMY_DATABASE_URI = 'mysql:///'+os.path.join(basedir, 'coba_db.db') #TODO
   
  
  HOST = str(os.environ.get("DB_HOST"))
  DATABASE = str(os.environ.get("DB_DATABASE"))
  USERNAME = str(os.environ.get("DB_USERNAME"))
  PASSWORD = str(os.environ.get("DB_PASSWORD"))
  
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_RECORD_QUERIES = True 
  
  

  
  
