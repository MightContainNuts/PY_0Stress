# pylint: disable=wrong-import-order
import dependencies
from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)


@app.route("/")

def home():
    return ("hello world")


# app.run(host="0.0.0.0", port=81)
 