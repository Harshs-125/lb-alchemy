from flask import Blueprint,request,jsonify
from controllers.members import addMember,removeMember
members=Blueprint('members',__name__)
@members.route('/add',methods=['POST'])
def add():
    request_data=request.json
    response=addMember(request_data['name'],request_data['email'])
    return jsonify({"response":response}),200

@members.route('/remove',methods=['POST'])
def remove():
    request_data=request.json
    response=removeMember(request_data['id'])
    return jsonify({"response":response}),200
