
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func


from packages import db

class Books(db.Model):
    __tablename__="books"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    author=db.Column(db.String(50),nullable=False)
    available=db.Column(db.Integer(),default=0)
    votes=db.Column(db.Integer(),nullable=False)
    def __init__(self ,name ,author,available,votes) :
        self.name=name
        self.author=author
        self.available=available
        self.votes=votes
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def find_max_votes():
        books=Books.query.all()
        books=sorted(books,'votes'=lambda x:x['votes'])
        print(books)

    def __repr__(self)  :
        return f"Book({self.id},{self.name},{self.author},{self.available})"



