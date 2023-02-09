from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from env.constants import SQL_ALCHEMY_DATABASE_URL
migrate=Migrate()

from routes.index import root


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=SQL_ALCHEMY_DATABASE_URL
db=SQLAlchemy()
db.init_app(app)
migrate.init_app(app,db)
app.register_blueprint(root)

if __name__=='__main__':
    app.run()


