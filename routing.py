from flask import Flask, redirect, url_for, request , render_template
import os

app = Flask(__name__)
app._static_folder = os.path.abspath("templates/static/")

@app.route("/")
def dashBoard():
    return render_template("index.html")

@app.route("/updateData" , methods=["POST"])
def updateData():
    print(request.json["Data"])
    return "GOT IT"



app.run(debug=True)