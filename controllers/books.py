from flask import Flask
import requests
from env.constants import BOOK_API_URL,X_RapidAPI_Host,X_RapidAPI_Key
from models.books import Books
from models.members import Members
from models.transactions import Transactions
from packages import db
def addbooks(genre):
    url = f"{BOOK_API_URL}{genre}/2020"
    headers = {
	    "X-RapidAPI-Key": "b403235f84msh4b8a7702e4c9501p1b3b58jsn3ab0b7b79b85",
	    "X-RapidAPI-Host": "hapi-books.p.rapidapi.com"
    }
    response = requests.get(url,headers=headers)
    arr = response.json()
    for book in arr:
        b=Books(name=book["name"],author=book["author"],available=20)
        db.session.add(b)
    db.session.commit()
    return arr

def borrowBook(data):
    member_id=data['member_id']
    book_id=data['book_id']
    member=Members.query.filter_by(id=member_id).first()
    book=Books.query.filter_by(id=book_id).first()
    transaction=Transactions.query.filter_by(member_id=member_id,book_id=book_id).first()
    if(transaction):
        return "this book is already issued to this member cannot reissue the same book "
    if(not member):
        return "no member found with this member id"
    
    if(not book):   
        return "no book with this book id in the library"
    transaction=Transactions(book_id,member_id)
    transaction.save()
    book.available=book.available-1
    book.save()
    return "book is issued to the member"

def editBook(data):
    book_id=data["book_id"]
    name=data['name']            

    
