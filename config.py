import os 

class Config:
    '''
    a method that provides general settings for application
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:silfanus12@localhost/pitch'

class ProdConfig(Config):
    '''
    Method that provides setting for production

    Args: 
         Permits child class to inherit from class Config
    '''
    pass
class DevConfig(Config):
    '''
    Method that sets configuarations for development class
    Args: 
         enable child class to inherit from parent class 
    '''

    DEBUG=True

config_options={
'production':ProdConfig,
'development':DevConfig
}