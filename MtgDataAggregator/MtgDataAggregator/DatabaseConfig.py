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

    def get_host(self):
        return self.host

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password

    def get_dbname(self):
        return self.dbname

    def get_port(self):
        return self.port

    def get_connection_string(self):
        return 'host=' + self.host + ' user=' + self.user + ' password=' + self.password + ' dbname=' + self.dbname + ' port=' + self.port

    




