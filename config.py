

class Config(object):
    SECRET_KEY = "you-will-never-guess"
    

class DevelopmentConfig(Config):
    DEBUG = True
    

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False