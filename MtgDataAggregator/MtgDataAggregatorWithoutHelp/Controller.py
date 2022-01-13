from mtgsdk import Set
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/sets")
def get_sets():
    response = Set.all()
    return response
