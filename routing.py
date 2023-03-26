from flask import Flask, redirect, url_for, request , render_template
import os
import crud

app = Flask(__name__)
app._static_folder = os.path.abspath("templates/static/")

@app.route("/" , methods=['POST'])
def dashBoard():
    data = crud.retrieve_Data()
    return render_template("index.html" , data=data)

@app.route("/updateData" , methods=["POST"])
def updateData():
    print(request.json["Data"])
    return "GOT IT"



app.run(debug=True)