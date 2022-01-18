from flask import Flask
from MtgAccess import MtgApiClient
import json

app = Flask(__name__)
app.debug = True


# get all sets and populate database
@app.route('/sets', methods=['GET'])
def get_sets():
    mtg_api_client = MtgApiClient.MtgApiClient()
    sets = mtg_api_client.get_sets()
    sets_json = json.dumps(sets)
    return sets_json
