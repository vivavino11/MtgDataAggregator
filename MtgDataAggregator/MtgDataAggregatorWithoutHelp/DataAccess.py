import psycopg2


class DataAccess:
    def __init__(self, configuration):
        self.configuration = configuration
        host = configuration.host
        user = self.configuration.user
        password = self.configuration.password
        dbname = self.configuration.dbname
        port = self.configuration.port
        self.connectionString = f'dbname={dbname} user={user} password={password} host={host} port={port}'

    def test(self):
        conn = psycopg2.connect(self.connectionString)
        cur = conn.cursor()
        cur.execute("SELECT * FROM \"Test\"")
        response = cur.fetchall()
        cur.close()
        conn.close()

