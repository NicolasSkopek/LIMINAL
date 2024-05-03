import os
from flask import Flask, render_template, url_for, redirect
import json
import random
import string

app = Flask(__name__)

def randomString(range1, range2):
    length = random.randint(range1, range2)
    return str(''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase +
                             string.digits, k=length)))

@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("desktop"))

@app.route("/desktop", methods=["GET"])
def desktop():
    with open("data.json") as f:
        data = f.read()
    spaces = json.loads(data)
    random.shuffle(spaces)

    path = "static/styles/audios/songs"
    files = os.listdir(path)
    songs = [file for file in files]
    random.shuffle(songs)
  
    return render_template("desktop.html", spaces=spaces, songs=songs, randomString=randomString)


if __name__ == '__main__':
    app.run(debug=True)

