from flask import Flask
from datetime import datetime,date
import requests
from env.constants import BOOK_API_URL,X_RapidAPI_Host,X_RapidAPI_Key
from models.books import Books
from models.members import Members
from models.transactions import Transactions
from models.members import Members
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
        b=Books(name=book["name"],author=book["author"],available=20,votes=book['votes'])
        db.session.add(b)
    db.session.commit()
    return arr

def borrowBook(data):
    member_id=data['member_id']
    book_id=data['book_id']
    member=Members.query.filter_by(id=member_id).first()
    book=Books.query.filter_by(id=book_id).first()
    transaction=Transactions.query.filter_by(member_id=member_id,book_id=book_id).first()
    if(transaction and transaction.status=="issued"):
        return "this book is already issued to this member cannot reissue the same book "
    if(not member):
        return "no member found with this member id"
    if(not book):   
        return "no book with this book id in the library"
    if(member.debt>=500):
        return "cannot issue the book since members dept is exceeding the limit"
    transaction=Transactions(book_id,member_id)
    member.hasbooks=member.hasbooks+1
    book.available=book.available-1
    book.votes=book.votes+1
    book.save()
    transaction.save()
    member.save()
    return "book is issued to the member"

def editBookData(data):
    book_id=data["book_id"]
    book=Books.query.filter_by(id=book_id).first()
    if(book): 
        if(data['key']=="name"):
          book.name=data['value']
        elif(data['key']=="author"):
            book.author=data['value']
        elif(data['key']=="available"):
            book.available=data['value']
        book.save()
        return "book details is edited"
    else:
        return "no book with the given id "
           
def returnBookData(data):
    transation_id=data['id']
    transaction=Transactions.query.filter_by(id=transation_id).first()
    member=Members.query.filter_by(id=transaction.member_id).first()
    book=Books.query.filter_by(id=transaction.book_id).first()
    amount_paid=data['amount_paid']
    if(transaction):
        issued_date=transaction.issue_date
        current_date=date.today()
        delta = current_date-issued_date
        days=delta.days
        amount_to_pay=100
        if(days>15):
            fine=((current_date-issued_date)-15)*10
            amount_to_pay=amount_to_pay+fine
        transaction.return_date=current_date
        transaction.amount_to_paid=amount_to_pay
        transaction.amount_paid=amount_paid
        transaction.status="returned"
        member.hasbooks=member.hasbooks-1
        book.available=book.available+1
        if(amount_to_pay-amount_paid>0):
             member.debt=member.debt+(amount_to_pay-amount_paid)
        member.save()
        transaction.save()
        book.save()
        return "successfully record the returned data "
    return "no such transaction found"

def mostPopular():
    book=Books.query.max(votes).first()
    print(book)
    return ""


      

    
