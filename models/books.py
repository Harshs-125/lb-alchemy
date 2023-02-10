
from flask_sqlalchemy import SQLAlchemy


from packages import db

class Books(db.Model):
    __tablename__="books"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    author=db.Column(db.String(50),nullable=False)
    available=db.Column(db.Integer(),default=0)
    def __init__(self ,name ,author,available) :
        self.name=name
        self.author=author
        self.available=available
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self)  :
        return f"Book({self.id},{self.name},{self.author},{self.available})"



