from flask import Blueprint,request,jsonify
from controllers.books import addbooks,borrowBook
books=Blueprint('books',__name__)
@books.route('/add',methods=['POST'])
def add():
    request_data=request.json
    response=addbooks(request_data['genre'])
    return jsonify({"response":response}),200


@books.route('/borrow',methods=['POST'])
def borrow():
    request_data=request.json
    response=borrowBook(request_data)
    return jsonify({
     "response":response
    }),200


    
