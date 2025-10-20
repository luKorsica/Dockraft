from flask import Flask
from flask_pymongo import PyMongo
from app.config import Config

mongo = PyMongo()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialiser MongoDB
    mongo.init_app(app)
    
    # Enregistrer les blueprints
    from app.routes.user_routes import user_bp
    from app.routes.server_routes import server_bp

    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(server_bp, url_prefix='/api')
    
    @app.route('/')
    def index():
        return {'message': 'API Flask MVC avec MongoDB', 'status': 'running'}
    
    return app