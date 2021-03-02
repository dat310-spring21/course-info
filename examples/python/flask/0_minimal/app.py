"""
Flask: A minimal web application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/test")
def test():
    return render_template("index.html", msg="my message", value=123, id="myid", color="lightblue")

if __name__ == "__main__":
    app.run()
