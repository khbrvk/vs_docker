from flask import Flask
from config import DockerConfig, LocalConfig
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from flask_migrate import Migrate
from flask_admin import Admin

engine = create_engine(DockerConfig.SQLALCHEMY_DATABASE_URI)
if not database_exists(engine.url):
    create_database(engine.url)
app = Flask(__name__)
app.config.from_object(DockerConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import Cat, UserAdmin
admin = Admin(app)
admin.add_view(UserAdmin(Cat, db.session))
import routes