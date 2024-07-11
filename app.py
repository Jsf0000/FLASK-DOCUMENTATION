from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()

ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'

    db.init_app(app)

    ## needs the imports
    from routes import register_routes
    register_routes(app, db)

    migrate = Migrate(app, db)

    return app

# flask --app FlaskUsePOST.py run   