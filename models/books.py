from sqlalchemy.dialects.sqlite import UUID
from flask_sqlalchemy import SQLAlchemy
import uuid
from ..app import db


class Books(db.model):
    __tablename__="books"
    id=db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name=db.Column(db.String(50),nullable=False)
    author=db.Column(db.String(50),nullable=False)
    publisher=db.Column(db.String(50),nullable=False)
    pages=db.Column(db.Integer(),nullable=False)
    # total_stock=db.Column(db.Integer(),default=0)
    available=db.Column(db.Integer(),default=0)
    # cost=db.Column(db.Integer(),nullable=False)
    def __init__(self ,name ,author,publisher,pages,available) :
        self.name=name
        self.author=author
        self.publisher=publisher
        self.pages=pages
        # self.total_stock=total_stock
        self.available=available
        # self.cost=cost
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self)  :
        return f"Book({self.id},{self.name},{self.author},{self.publisher},{self.pages},{self.total_stock},{self.available},{self.cost})"



