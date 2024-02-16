import os
from flask import Flask, render_template, url_for, redirect
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("desktop"))

@app.route("/desktop", methods=["GET"])
def desktop():
    with open("data.json") as f:
        data = f.read()
    spaces = json.loads(data)

    path = "static/styles/audios/songs"
    files = os.listdir(path)
    songs = [file for file in files]
  
    return render_template("desktop.html", spaces=spaces, songs=songs)

if __name__ == '__main__':
    app.run(debug=True)