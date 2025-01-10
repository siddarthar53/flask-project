from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
DB_NAME="database.db"

#initalising a flask app
def create_app():
	app=Flask(__name__)
	app.config["SECRET_KEY"]="sid"
	app.config["SQLALCHEMY_DATABASE_URI"]=f'sqlite:///{DB_NAME}'
	db.init_app(app)

	from .auth import auth
	from .views import views
	app.register_blueprint(auth,url_prefix='/')
	app.register_blueprint(views,url_prefix='/')
	return app