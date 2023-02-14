
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
        return f"Transaction( id={self.id}, book_id={self.book_id}, member_id={self.member_id}, issue_data={self.issue_date}, return_data={self.return_date}, amount_paid={self.amount_paid}, amount_to_paid={self.amount_to_paid}, status={self.status})"



