from flask import Flask
import requests
from env.constants import BOOK_API_URL,X_RapidAPI_Host,X_RapidAPI_Key
from models.books import Books
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