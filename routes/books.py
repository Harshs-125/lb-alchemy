from flask import Blueprint,request,jsonify
from controllers.books import addbooks
books=Blueprint('books',__name__)
@books.route('/add',methods=['POST'])
def add():
    request_data=request.json
    response=addbooks(request_data['genre'])
    return jsonify({"response":response}),200


