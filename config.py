import os

class Config:
  '''
  General configuration parent class 
  '''
  # QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://faithrehema:fefe@localhost/blog'

  SQLALCHEMY_TRACK_MODIFICATIONS = True
  SECRET_KEY = 'fefe'
  UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
  '''
  Production configuration child class
  Args:
      Config: The parent configuration class with General configuration settings 
  '''
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
  '''
  Development configuration child class 
  Args:
    Config: The parent configuration class with General configuration settings 
  '''

  DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig
}