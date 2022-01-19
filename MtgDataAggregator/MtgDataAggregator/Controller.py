# $env:FLASK_APP = "Controller.py"
# $env:FLASK_ENV = "development"

from flask import Flask, url_for
from flask import request

from BusinessComponent import BusinessComponent
from DataAccess import DataAccess
from DatabaseConfig import DatabaseConfig


app = Flask(__name__)
app.debug = True


@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'


@app.route('/collections', methods=['GET'])
def get_collections():
    try:
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = BusinessComponent(data_access)
        collections = business_component.get_collections()
        if len(collections) == 0:
            return 'Collection Not Found', 404
        return collections, 200
    except Exception as e:
        return str(e), 500


@app.route('/collections', methods=['POST'])
def create_collection():
    try:
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = BusinessComponent(data_access)
        collection = business_component.add_collection(request.json)
        if collection is None:
            return 'Collection Not Created', 500
        return collection, 201
    except Exception as e:
        return str(e), 500


@app.route('/collections/<collection_id>', methods=['GET'])
def get_collection(collection_id):
    try:
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = BusinessComponent(data_access)
        collection = business_component.get_collection_by_id(collection_id)
        if collection is None:
            return 'Collection Not Found', 404
        return collection, 200
    except Exception as e:
        return str(e), 500


@app.route('/collections/<collection_id>/locations', methods=['GET'])
def get_collection_locations(collection_id):
    try:
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = BusinessComponent(data_access)
        locations = business_component.get_locations(collection_id)
        if len(locations) == 0:
            return 'Collection Not Found', 404
        return locations, 200
    except Exception as e:
        return str(e), 500


@app.route('/collections/<collection_id>/locations', methods=['POST'])
def create_collection_location(collection_id):
    try:
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = BusinessComponent(data_access)
        location = business_component.add_location(collection_id, request.json)
        if location is None:
            return 'Location Not Created', 500
        return location, 201
    except Exception as e:
        return str(e), 500


@app.route('/collections/<collection_id>/locations/<location_id>', methods=['GET'])
def get_collection_location(collection_id, location_id):
    try:
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = BusinessComponent(data_access)
        location = business_component.get_location_by_id(collection_id, location_id)
        if location is None:
            return 'Location Not Found', 404
        return location, 200
    except Exception as e:
        return str(e), 500

@app.route('/collections/<collection_id>/locations/<location_id>/cards', methods=['GET'])
def get_collection_location_cards(collection_id, location_id):
    try:
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = BusinessComponent(data_access)
        cards = business_component.get_cards(collection_id, location_id)
        if len(cards) == 0:
            return 'Location Not Found', 404
        return cards, 200
    except Exception as e:
        return str(e), 500


@app.route('/collections/<collection_id>/locations/<location_id>/cards', methods=['POST'])
def create_collection_location_card(collection_id, location_id):
    try:
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = BusinessComponent(data_access)
        card = business_component.add_card(collection_id, location_id, request.json)
        if card is None:
            return 'Card Not Created', 500
        return card, 201
    except Exception as e:
        return str(e), 500


@app.route('/collections/<collection_id>/locations/<location_id>/cards/<card_id>', methods=['GET'])
def get_collection_location_card(collection_id, location_id, card_id):
    try:
        configuration = DatabaseConfig()
        data_access = DataAccess(configuration)
        business_component = BusinessComponent(data_access)
        card = business_component.get_card_by_id(collection_id, location_id, card_id)
        if card is None:
            return 'Card Not Found', 404
        return card, 200
    except Exception as e:
        return str(e), 500