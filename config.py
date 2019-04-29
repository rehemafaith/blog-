import os

class Config:
  '''
  General configuration parent class 
  '''
  QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://faithrehema:fefe@localhost/blog'
class ProdConfig(Config):
  '''
  Production configuration child class
  Args:
      Config: The parent configuration class with General configuration settings 
  '''
  pass

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