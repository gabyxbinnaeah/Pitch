class Config:
    '''
    a method that provides general settings for application
    '''

class ProdConfig(Config):
    '''
    Method that provides setting for proction

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
'development':DeveConfig
}