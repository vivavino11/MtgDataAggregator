import configparser


class DatabaseConfig:
    host = ''
    user = ''
    password = ''
    dbname = ''
    port = ''

    def __init__(self, config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        self.host = config['postgresql']['host']
        self.user = config['postgresql']['user']
        self.password = config['postgresql']['password']
        self.dbname = config['postgresql']['dbname']
        self.port = config['postgresql']['port']
