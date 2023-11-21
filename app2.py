from flask import Flask,jsonify,request

app = Flask(__name__)

books=[
    {"id":1,"title":"Book1"},
    {"id":2,"title":"Book2"},
    {"id":3,"title":"Book3"},
    {"id":4,"title":"Book4"},
    {"id":5,"title":"Book5"}
]

@app.route("/books",methods=['GET'])
def get_books():
    return books

@app.route("/books/<int:bookid>",methods=['GET'])
def get_book(bookid):
  for i in books:
    if i["id"] == bookid:
      return jsonify(i)
  else:
      return jsonify({"message":"book not found"}),404 

@app.route("/books/",methods=['POST'])
def create_book():
  data= request.get_json()
  books.append({"id":len (books)+1,"title":data["title"]})
  
  return jsonify({"message":"book successfully added"}),201 

@app.route("/books/",methods=['DELETE'])
def delete_book():
  data= request.get_json()
  for i in books:
     if i["title"]== data["title"] :
        books.remove({"id":i["id"],"title":i["title"]})
  return jsonify({"message":"book successfully deleted"}),201

@app.route("/books/<int:bookid>",methods=['PUT'])
def update_book(bookid):
  data= request.get_json()
  for i in books:
     if i["id"]== bookid:
        i["title"]=data["title"]
        
  return jsonify({"message":"book successfully updated"}),201 

  
if __name__=="__main__":
    app.run(debug=False,host="172.25.110.97")