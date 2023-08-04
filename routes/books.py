from flask import Blueprint,request,jsonify
from controllers.books import addbooks,borrowBook,editBookData,returnBookData,mostPopular,getbooks
books=Blueprint('books',__name__)

@books.route('/get',methods=['GET'])
def getbook():
    response=getbooks();
    return jsonify({"response":response}),200

@books.route('/add',methods=['POST'])
def add():
    response=addbooks("romance")
    return jsonify({"response":"suucessfully added books "}),200

@books.route('/borrow',methods=['POST'])
def borrow():
    request_data=request.json
    response=borrowBook(request_data)
    return jsonify({
     "response":response
    }),200

@books.route('/edit-book-data',methods=['PATCH'])
def edit():
    request_data=request.json
    response=editBookData(request_data)
    return jsonify({
        "response":response
    }),200

    
@books.route('/return',methods=['POST'])
def returnBook():
    request_data=request.json
    response=returnBookData(request_data)
    return jsonify({
        "response":response
    }),200

@books.route('/popular',methods=['GET'])
def mostpopular():
    response=mostPopular()
    return jsonify({
        "response":response
    }),200