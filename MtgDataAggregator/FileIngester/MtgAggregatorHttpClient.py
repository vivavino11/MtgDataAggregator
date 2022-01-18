from MtgAggregatorClientInterface import MtgAggregatorClientInterface


class MtgAggregatorHttpClient(MtgAggregatorClientInterface):
    def __init__(self, configuration):
        self.url = configuration.mtg_aggregator_url

    def add_card_to_collection(self, card, collection, location, quantity):
        raise NotImplementedError
