from flask import Flask
from env.constants import SQL_ALCHEMY_DATABASE_URL
from routes.index import root
from routes.books import books
from packages import db , migrate
def app_init():

    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']=SQL_ALCHEMY_DATABASE_URL
    
    db.init_app(app)
    migrate.init_app(app,db)
    app.register_blueprint(root)
    app.register_blueprint(books,url_prefix='/book')
    return app 
    