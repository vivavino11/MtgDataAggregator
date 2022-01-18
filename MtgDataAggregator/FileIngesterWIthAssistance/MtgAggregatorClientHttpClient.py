from MtgAggregatorClientInterface import MtgAggregatorClientInterface


class MtgAggregatorHttpClient(MtgAggregatorClientInterface):
    def __init__(self):
        self.url = "http://mtgaggregator.com/api/v1/cards"

    def add_card_to_collection(self, card, collection, location, quantity):
        raise NotImplementedError

