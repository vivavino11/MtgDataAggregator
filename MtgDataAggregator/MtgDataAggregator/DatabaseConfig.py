import configparser


class DatabaseConfig:
    host = ''
    user = ''
    password = ''
    dbname = ''
    port = ''

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('Config/db.ini')
        self.host = config['postgresql']['host']
        self.user = config['postgresql']['user']
        self.password = config['postgresql']['password']
        self.dbname = config['postgresql']['dbname']
        self.port = config['postgresql']['port']
