from flask import Flask
import requests
from models.members import Members
from models.transactions import Transactions
from packages import db

def addMember(name,email):
    mem=Members.query.filter_by(email=email).first()
    if(mem):
        return "member already exits"
    member=Members(name,email)
    member.save()
    return "member added successfully"

def removeMember(id):
    mem=Members.query.filter_by(id=id).first()
    if(mem):
        db.session.delete(mem)
        mem.save()
        return "member removed successfully"
    return "no member exits with this id"

def history(id):
    member=Members.query.filter_by(id=id).first()
    arr=[]
    if(member):
        transactions=Transactions.query.filter_by(member_id=id).all()
        for transaction in transactions:
            arr.append(transaction.__repr__())
        return {'transactions':arr,'debt':member.debt,'total_books':member.hasbooks}
    return "no member with this id "
def payDebt(id,amount):
    member=Members.query.filter_by(id=id).first()
    if(member):
        member.debt=member.debt-amount
        member.save()
        return "successfully register the amount"
    return "no memeber with this id"

