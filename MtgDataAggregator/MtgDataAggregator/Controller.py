from flask import Flask, jsonify
from MtgAccess import MtgApiClient
import json

app = Flask(__name__)
app.debug = True


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/sets")
def get_sets():
    mtg_access = MtgApiClient()
    response = mtg_access.GetAllSets()
    return json.dumps(response)
