from Mapper import *


class MtgDataAggregatorBusinessComponent:
    def __init__(self, data_access):
        self.data_access = data_access

    def get_collections(self):
        all_domain_collections = self.data_access.get_collections()
        collections = map_domain_collection_list_to_model_collections_list(all_domain_collections)
        return collections

    def get_collection_by_name(self, collection_name):
        domain_collection = self.data_access.get_collection_by_name(collection_name)
        collection = map_domain_collection_to_model_collection(domain_collection)
        return collection

    def get_collection_by_id(self, collection_id):
        domain_collection = self.data_access.get_collection_by_id(collection_id)
        collection = map_domain_collection_to_model_collection(domain_collection)
        return collection

    def add_collection(self, collection_name):
        collection_id = self.data_access.add_collection(collection_name)
        return collection_id

    def get_locations(self, collection_id):
        domain_locations = self.data_access.get_locations(collection_id)
        locations = map_domain_location_list_to_model_location_list(domain_locations)
        return locations

    def get_location_by_name(self, collection_id, location_name):
        domain_location = self.data_access.get_location_by_name(collection_id, location_name)
        location = map_domain_location_to_model_location(domain_location)
        return location

    def get_location_by_id(self, location_id):
        domain_location = self.data_access.get_location_by_id(location_id)
        location = map_domain_location_to_model_location(domain_location)
        return location

    def add_location(self, collection_id, location):
        location_id = self.data_access.add_location(collection_id, location.name, location.description)
        return location_id

    def get_cards(self, collection_id, location_id):
        domain_card_list = self.data_access.get_cards(collection_id, location_id)
        card_list = map_domain_card_list_to_model_card_list(domain_card_list)
        return card_list

    def get_card(self, collection_id, location_id, card_id):
        domain_card = self.data_access.get_card(collection_id, location_id, card_id)
        card = map_domain_card_to_model_card(domain_card)
        return card

    def add_card(self, collection_id, location_id, card):
        card_id = self.data_access.insert_card(collection_id, location_id, card)
        return card_id


