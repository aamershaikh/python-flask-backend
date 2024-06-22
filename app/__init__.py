from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('app.config.Config')

    # Initialize SQLAlchemy
    db.init_app(app)

    # Import and register blueprints
    from app.user.user_routes import user_blueprint
    from app.account.account import account_blueprint
    app.register_blueprint(user_blueprint)
    app.register_blueprint(account_blueprint)

    # Create tables
    with app.app_context():
        db.create_all()

    return app
