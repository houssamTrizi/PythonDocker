from urllib.parse import quote_plus


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite//:memory:"
    SQLALCHEMY_POOL_TIMEOUT = 60
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = fr"mysql://root:{quote_plus('p@ssw0rd1')}@127.0.0.1:3306/inventory"


class DevConfig(Config):
    DEBUG = True


class TestingConfig(DevConfig):
    TESTING = True


config = {
    "prod": ProductionConfig,
    "dev": DevConfig,
    "testing": TestingConfig
}
