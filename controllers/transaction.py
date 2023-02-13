from flask import Flask
from datetime import date,datetime
import requests

from models.transactions import Transactions
from packages import db
def viewrecord(data):
    transaction=Transactions.query.filter_by(id=data['id']).first()
    if(transaction):
        issued_date=transaction.issue_date
        current_date=date.today()
        delta = current_date-issued_date
        days=delta.days
        amount_to_pay=100
        if(days>15):
            fine=((current_date-issued_date)-15)*10
            amount_to_pay=amount_to_pay+fine
        return f"transaction {transaction.id} {transaction.book_id} {transaction.member_id} amount to pay : {amount_to_pay}"
    return "no transaction with this id "


