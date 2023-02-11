
from flask_sqlalchemy import SQLAlchemy


from packages import db

class Members(db.Model):
    __tablename__="members"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(50),nullable=False,unique=True)
    hasbooks=db.Column(db.Integer,nullable=False,default=0)
    amount=db.Column(db.Integer,nullable=False,default=0)
    def __init__(self ,name,email) :
        self.name=name
        self.email=email
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self)  :
        return f"Book({self.id},{self.name},{self.email},{self.hasbooks},{self.amount})"



