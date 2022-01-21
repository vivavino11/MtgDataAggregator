# $env:FLASK_APP = "Controller.py"
# $env:FLASK_ENV = "development"

from flask import Flask, jsonify, url_for
from flask import request

from Models.Card import Card
from Models.Location import Location
from MtgDataAggregatorBusinessComponent import MtgDataAggregatorBusinessComponent
from DataAccess import DataAccess
from DatabaseConfig import DatabaseConfig


app = Flask(__name__)
app.debug = True


@app.route("/ping")
def hello_world():
    return "Hello, World!"


@app.route("/collections", methods=['GET'])
def get_collections():
    try:
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = MtgDataAggregatorBusinessComponent(data_access)
        collections = business_component.get_collections()
        if len(collections) == 0:
            return "No Collections Found", 404
        else:
            return jsonify(collections), 200
    except Exception as ex:
        # ToDo: Add Logging
        return "Internal Server Error", 500


@app.route("/collections/<collection_id>", methods=["GET"])
def get_collection_by_id(collection_id):
    try:
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = MtgDataAggregatorBusinessComponent(data_access)
        collection = business_component.get_collection_by_id(collection_id)
        if collection is None:
            return "No Collection Found", 404
        else:
            return jsonify(collection), 200
    except Exception as ex:
        # ToDo: Add Logging
        return "Internal Server Error", 500


@app.route("/collections", methods=['POST'])
def add_collection():
    try:
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = MtgDataAggregatorBusinessComponent(data_access)
        created_collection_id = business_component.add_collection(request.json['name'])
        return url_for('get_collection_by_id', collection_id=created_collection_id), 201
    except Exception as e:
        # ToDo: Add Logging
        return "Internal Server Error", 500


@app.route("/collections/<collection_id>/locations", methods=['GET'])
def get_locations(collection_id):
    try:
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = MtgDataAggregatorBusinessComponent(data_access)
        locations = business_component.get_locations(collection_id)
        if len(locations) == 0:
            return "No Collection Found", 404
        else:
            return jsonify(locations), 200
    except Exception as ex:
        # ToDo: Add Logging
        return "Internal Server Error", 500


@app.route("/collections/<collection_id>/locations/<location_id>", methods=['GET'])
def get_location_by_id(collection_id, location_id):
    try:
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = MtgDataAggregatorBusinessComponent(data_access)
        location = business_component.get_location_by_id(location_id)
        if location is None:
            return "No lcoation found", 404
        else:
            return jsonify(location), 200
    except Exception as ex:
        # ToDo: Add Logging
        return "Internal Server Error", 500


@app.route("/collections/<collection_id>/locations", methods=['POST'])
def add_location(collection_id):
    try:
        raw_location = Location(request.json['name'], request.json['description'])
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = MtgDataAggregatorBusinessComponent(data_access)
        created_location_id = business_component.add_location(collection_id, raw_location)
        return url_for('get_location_by_id', collection_id=collection_id, location_id=created_location_id), 201
    except Exception as ex:
        return "Internal Server Error", 500


@app.route("/collections/<collection_id>/locations/<location_id>/cards", methods=['GET', 'POST'])
def get_cards(collection_id, location_id):

    try:
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = MtgDataAggregatorBusinessComponent(data_access)
        cards = business_component.get_cards(collection_id, location_id)
        if len(cards) == 0:
            return "No Cards Found", 404
        else:
            return jsonify(cards), 200
    except Exception as ex:
        # ToDo: Add Logging
        return "Internal Server Error", 500


@app.route("/collections/<collection_id>/locations/<location_id>/cards/<card_id>", methods=['GET'])
def get_card_by_id(collection_id, location_id, card_id):
    try:
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = MtgDataAggregatorBusinessComponent(data_access)
        card = business_component.get_card(collection_id, location_id, card_id)
        if card is None:
            return "No card found", 404
        else:
            return jsonify(card), 200
    except Exception as ex:
        # ToDo: Add Logging
        return str(ex), 500
        return "Internal Server Error", 500


@app.route("/collections/<collection_id>/locations/<location_id>/cards", methods=["POST"])
def add_card(collection_id, location_id):
    try:
        raw_card = Card(request.json['name'], request.json['edition'], request.json['condition'], request.json['is_foil'])
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = MtgDataAggregatorBusinessComponent(data_access)
        created_card_id = business_component.add_card(collection_id, location_id, raw_card)
        return url_for('get_card_by_id', collection_id=collection_id,
                   location_id=location_id, card_id=created_card_id), 201
    except Exception as ex:
        # ToDo: Add Logging
        return "Internal Server Error", 500

