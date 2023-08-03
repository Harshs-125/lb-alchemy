from flask import Flask
from env.constants import SQL_ALCHEMY_DATABASE_URL
from routes.index import root
from routes.books import books
from routes.members import members
from routes.transacions import transaction
from packages import db , migrate
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

def app_init():

    app=Flask(__name__)
    username = 'root'
    password = 'harsh@123'
    encoded_username = quote(username)
    encoded_password = quote(password)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{encoded_username}:{encoded_password}@localhost/library'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    # migrate.init_app(app,db)
    app.register_blueprint(root)
    app.register_blueprint(books,url_prefix='/book')
    app.register_blueprint(members,url_prefix='/member')
    app.register_blueprint(transaction,url_prefix='/transaction')   
    with app.app_context() :
        db.create_all()
    return app 
    