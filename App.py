# import modules

from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
# initialize database


# create your routes here

# initializes app


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/socialMedia"
mongo = PyMongo(app)


@app.route("/", methods=["GET","POST"])
def home():
    tweets = mongo.db.socialMedia.find()
    if request.method == "POST":
        name = request.form["name"]
        title = request.form["title"]
        message = request.form["message"]
        mongo.db.socialMedia.insert({"title":title, "name":name,"message":message})
        
    return render_template("home.html", tweets=tweets)

# @app.route("/what", methods=["GET"])
# def what():
#     return "hello"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)

# @app.route("/addNewProperty", methods=["POST"])
# def getPropertyFrom():

        



