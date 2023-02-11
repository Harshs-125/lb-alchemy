from flask import Flask
import requests
from models.members import Members
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