from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from flask_caching import Cache
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_babel import Babel

from .core.settings import config


base_dir = Path(__file__).resolve().parent

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()
# toolbar = DebugToolbarExtension()
cache = Cache()
admin = Admin()
admin.name = "Flask Admin"
admin.template_mode = "bootstrap4" # Bootstrap(2, 3, 4)
admin.index_view._template = "admin/index.html"
admin.base_template = "admin/base.html"

babel = Babel()


def create_app(config_class: str = "app.core.settings.config"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    cache.init_app(app)
    babel.init_app(app)

    login_manager.login_view = "routes.auth.login"

    if config.DEBUG:
        admin.init_app(app)

        from app.models import (
            User, About, Stats, Skils, Resume
        )
        admin.add_view(ModelView(User, db.session))
        admin.add_view(ModelView(About, db.session))
        admin.add_view(ModelView(Stats, db.session))
        admin.add_view(ModelView(Skils, db.session))
        admin.add_view(ModelView(Resume, db.session))
    
    from app import routes
    
    app.register_blueprint(routes.site_dp)
    app.register_blueprint(routes.auth_dp)
    
    return app
