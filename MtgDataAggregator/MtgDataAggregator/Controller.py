# $env:FLASK_APP = "Controller.py"
# $env:FLASK_ENV = "development"

from flask import Flask, jsonify, url_for
from flask import request
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
        if collections is None:
            return "No Collections Found", 404
        else:
            return collections, 200
    except Exception as ex:
        # ToDo: Add Logging
        return "Internal Server Error", 500


@app.route("/collections/<collection_id>)", methods=["GET"])
def get_collection_by_id(collection_id):
    try:
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = MtgDataAggregatorBusinessComponent(data_access)
        collection = business_component.get_collection_by_id(collection_id)
        if collection is None:
            return "No Collection Found", 404
        else:
            return collection, 200
    except Exception as ex:
        # ToDo: Add Logging
        return "Internal Server Error", 500


@app.route("/collections", methods=['POST'])
def add_collection():
    try:
        collection = request.form["collection"]
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = MtgDataAggregatorBusinessComponent(data_access)
        created_collection_id = business_component.add_collection(collection.name)
        return url_for(get_collection_by_id, collection_id=created_collection_id), 201
    except Exception as ex:
        # ToDo: Add Logging
        return "Internal Server Error", 500


@app.route("/collections/<collection_id>/locations", methods=['GET'])
def get_locations(collection_id):
    try:
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = MtgDataAggregatorBusinessComponent(data_access)
        collection = business_component.get_locations(collection_id)
        if collection is None:
            return "No Collection Found", 404
        else:
            return collection, 200
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
            return location, 200
    except Exception as ex:
        # ToDo: Add Logging
        return "Internal Server Error", 500


@app.route("/collections/<collection_id>/locations", methods=['POST'])
def add_location(collection_id):
    try:
        location = request.form["location"]
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = MtgDataAggregatorBusinessComponent(data_access)
        created_location_id = business_component.add_location(collection_id, location)
        return url_for(get_location_by_id, location=created_location_id), 201
    except Exception as ex:
        # ToDo: Add Logging
        return "Internal Server Error", 500
    return "test"


@app.route("/collections/<collection_id>/locations/<location_id>/cards", methods=['GET', 'POST'])
def get_cards_or_add_card(collection_id, location_id):
    if request.method == 'POST':
        try:
            card = request.form["card"]
            configuration = DatabaseConfig()
            data_access = DataAccess(configuration)
            business_component = MtgDataAggregatorBusinessComponent(data_access)
            created_card_id = business_component.add_card(collection_id, location_id, card)
            return url_for(get_card, collection_id=collection_id,
                           location_id=location_id, card_id=created_card_id), 201
        except Exception as ex:
            # ToDo: Add Logging
            return "Internal Server Error", 500
    else:
        try:
            configuration = DatabaseConfig()
            data_access = DataAccess(configuration)
            business_component = MtgDataAggregatorBusinessComponent(data_access)
            cards = business_component.get_cards(collection_id, location_id)
            if cards is None:
                return "No Cards Found", 404
            else:
                return cards, 200
        except Exception as ex:
            # ToDo: Add Logging
            return "Internal Server Error", 500


@app.route("/collections/<collection_id>/locations/<location_id>/cards/<card_id>", methods=['GET'])
def get_card(collection_id, location_id, card_id):
    try:
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = MtgDataAggregatorBusinessComponent(data_access)
        card = business_component.get_card(collection_id, location_id, card_id)
        if card is None:
            return "No card found", 404
        else:
            return card, 200
    except Exception as ex:
        # ToDo: Add Logging
        return "Internal Server Error", 500


