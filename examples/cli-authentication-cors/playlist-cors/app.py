# This app only handles AJAX requests.
# Open dist/index.html in browser.

from time import sleep
from flask import Flask, request, session
from flask_cors import CORS, cross_origin
import json




app = Flask(__name__)
CORS(app)
app.secret_key = "any random string"


PLAYLIST = [
        { "name": "My favorite",
          "band": "This band"
        },
        { "name": "Second favorite",
          "band": "This other band"
        }
    ]

@app.after_request
def add_header(response):
    # response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = "PUT,POST,GET,DELETE,OPTIONS"
    response.headers['Access-Control-Allow-Headers'] = "Content-Type,Content-Length, Authorization"
    return response

@app.route("/playlist", methods=["GET"])
def getplace():
    print("count is {}".format(session.get("count", "not there")))
    count = session.get("count", 0)
    session["count"] = count + 1
    print("count is now {}".format(session.get("count", "not there")))
    return json.dumps(PLAYLIST)

@app.route("/add", methods=["POST"])
def addSong():
    print("count is {}".format(session.get("count", "not there")))
    count = session.get("count", 0)
    session["count"] = count + 1
    print("count is now {}".format(session.get("count", "not there")))
    song = json.loads(request.data)
    if song not in PLAYLIST:
        PLAYLIST.append(song)
    return json.dumps(PLAYLIST)

@app.route("/remove", methods=["POST"])
def removeSong():
    print("count is {}".format(session.get("count", "not there")))
    count = session.get("count", 0)
    session["count"] = count + 1
    print("count is now {}".format(session.get("count", "not there")))
    song = request.get_json()
    print(song)
    if song in PLAYLIST:
        PLAYLIST.remove(song)
        
    return json.dumps(PLAYLIST)

if __name__ == "__main__":
    app.run(debug=True)