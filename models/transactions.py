
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from packages import db

class Transactions(db.Model):
    __tablename__="transactions"
    id=db.Column(db.Integer,primary_key=True)
    book_id=db.Column(db.Integer,nullable=False)
    member_id=db.Column(db.Integer,nullable=False)
    issue_date=db.Column(db.Date,nullable=False,default=datetime.now().date())
    return_date=db.Column(db.Date,default=None)
    status=db.Column(db.String,default="issued")
    amount_to_paid=db.Column(db.Integer,default=0)
    amount_paid=db.Column(db.Integer,default=0)
    def __init__(self ,book_id,member_id) :
        self.book_id=book_id
        self.member_id=member_id
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self)  :
        return f"Transaction({self.id},{self.book_id},{self.member_id},{self.issue_date},{self.return_date},{self.amount})"



