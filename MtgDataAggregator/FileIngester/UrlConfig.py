import configparser


class UrlConfig:
    mtg_aggregator_url = ''

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('Config/url.ini')
        self.mtg_aggregator_url = config['MtgAggregatorUrl']['url']