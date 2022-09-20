from flask import Flask

import dependencies

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World ! \n\n Checking Push on commit </p>"


# app.run(host="0.0.0.0", port=81)
