from flask import Flask, jsonify
from flask import request
from MtgDataAggregatorBusinessComponent import MtgDataAggregatorBusinessComponent
from DataAccess import DataAccess
from DatabaseConfig import DatabaseConfig
import json

app = Flask(__name__)
app.debug = True


@app.route("/ping")
def hello_world():
    return "Hello, World!"


@app.route("/collections", methods=['GET'])
def get_collections():
    return "test"


@app.route("collections/<collection_name>", methods=['POST'])
def add_collection(collection_name):
    return "test"


@app.route("/<collection_name>/locations", methods=['GET'])
def get_locations(collection_name):
    return "test"


@app.route("/<collection_name>/locations/<location_name>", methods=['POST'])
def add_location(collection_name, location_name):
    return "test"


@app.route("/<collection_name>/<location_name>/cards", methods=['GET', 'POST'])
def add_card(collection_name, location_name):
    if request.method == 'POST':
        try:
            card = request.form["card"]
            configuration = DatabaseConfig()
            data_access = DataAccess(configuration)
            business_component = MtgDataAggregatorBusinessComponent(data_access)
            return business_component.add_card(card, collection_name, location_name)
        except Exception as ex:
            # ToDo: Add Logging
            return "Internal Server Error", 500
    else:
        try:
            configuration = DatabaseConfig()
            data_access = DataAccess(configuration)
            business_component = MtgDataAggregatorBusinessComponent(data_access)
            cards = business_component.get_cards(collection_name, location_name)
            if cards is None:
                return "No Cards Found", 404
            else:
                return cards
        except Exception as ex:
            # ToDo: Add Logging
            return "Internal Server Error", 500


@app.route("/<collection_name>/<location_name>/cards/<id>", methods=['GET', 'PUT'])
def add_cards():
    if request.method == 'PUT':
        raise NotImplementedError
    else:
        raise NotImplementedError
