class MtgDataAggregatorBusinessComponent:
    def __init__(self, data_access):
        self.data_access = data_access

    def add_card(self, card, collection_name, location_name):
        return self.data_access.insert_card(collection_name, location_name, card)

    def get_cards(self, collection_name, location_name):
        return self.data_access.get_cards(collection_name, location_name)
