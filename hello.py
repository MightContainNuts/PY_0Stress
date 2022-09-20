import dependencies
from flask import Flask



app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World !</p>"
    return "<p>Checking Push on commit</p>"


# app.run(host="0.0.0.0", port=81)
