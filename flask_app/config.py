class LocalConfig(object):

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:135790qwerty@localhost:5432/skillbox_app2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '123213123sadasd'


class DockerConfig(object):

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@db:5432/skillbox_app2'