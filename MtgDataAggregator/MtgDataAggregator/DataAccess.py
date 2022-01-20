import psycopg2
from Domain.Card import Card
from Domain.Collection import Collection
from Domain.Location import Location


class DataAccess:
    def __init__(self, configuration):
        self.configuration = configuration
        host = configuration.get_host()
        database = configuration.get_dbname()
        user = configuration.get_user()
        password = configuration.get_password()
        port = configuration.get_port()
        self.connection = psycopg2.connect(host=host, database=database, user=user, password=password, port=port)

        self.get_collections_query = "SELECT * FROM collections"
        self.get_collection_by_id_query = "SELECT * FROM collections WHERE collection_id = %s"
        self.get_collection_by_name_query = "SELECT * FROM collections WHERE name = %s"
        self.add_collection_query = "INSERT INTO collections (name) VALUES (%s) RETURNING collection_id"

        self.get_locations_query = "SELECT * FROM locations WHERE collection_id = %s"
        self.get_location_by_id_query = "SELECT * FROM locations WHERE collection_id = %s AND location_id = %s"
        self.get_location_by_name_query = "SELECT * FROM locations WHERE collection_id = %s AND name = %s"
        self.add_location_query = "INSERT INTO locations (collection_id, name, description) VALUES (%s, %s, " \
                                  "%s) RETURNING location_id "

        self.get_cards_query = "SELECT * FROM cards WHERE collection_id = %s AND location_id = %s"
        self.get_card_by_id_query = "SELECT * FROM cards WHERE collection_id = %s AND location_id = %s AND card_id = %s"
        self.get_card_by_name_query = "SELECT * FROM cards WHERE collection_id = %s AND location_id = %s AND name = %s"
        self.add_card_query = "INSERT INTO cards (collection_id, location_id, name, edition, condition, is_foil) " \
                              "VALUES (%s, %s, %s, %s, %s, %s) RETURNING card_id "

    def __del__(self):
        self.connection.close()

    def get_collections(self):
        with self.connection.cursor() as cursor:
            cursor.execute(self.get_collections_query)
            collections = []
            for row in cursor:
                collection = Collection(row[0], row[1])
                collections.append(collection)
            return collections

    def get_collection_by_id(self, collection_id):
        with self.connection.cursor() as cursor:
            cursor.execute(self.get_collection_by_id_query, (collection_id,))
            row = cursor.fetchone()
            collection = Collection(row[0], row[1])
            return collection

    def get_collection_by_name(self, name):
        with self.connection.cursor() as cursor:
            cursor.execute(self.get_collection_by_name_query, (name,))
            row = cursor.fetchone()
            collection = Collection(row[0], row[1])
            return collection

    def add_collection(self, name):
        with self.connection.cursor() as cursor:
            cursor.execute(self.add_collection_query, (name,))
            row = cursor.fetchone()
            collection = Collection(row[0], name)
            self.connection.commit()
            return collection.collection_id

    def get_locations(self, collection_id):
        with self.connection.cursor() as cursor:
            cursor.execute(self.get_locations_query, (collection_id,))
            locations = []
            for row in cursor:
                location = Location(row[0], row[1], row[2])
                locations.append(location)
            return locations

    def get_location_by_id(self, collection_id, location_id):
        with self.connection.cursor() as cursor:
            cursor.execute(self.get_location_by_id_query, (collection_id, location_id))
            row = cursor.fetchone()
            location = Location(row[0], row[1], row[2])
            return location

    def get_location_by_name(self, collection_id, name):
        with self.connection.cursor() as cursor:
            cursor.execute(self.get_location_by_name_query, (collection_id, name))
            row = cursor.fetchone()
            location = Location(row[0], row[1], row[2])
            return location

    def add_location(self, collection_id, name, description):
        with self.connection.cursor() as cursor:
            cursor.execute(self.add_location_query, (collection_id, name, description))
            row = cursor.fetchone()
            location = Location(row[0], name, description, collection_id)
            self.connection.commit()
            return location.location_id

    def get_cards(self, collection_id, location_id):
        with self.connection.cursor() as cursor:
            cursor.execute(self.get_cards_query, (collection_id, location_id))
            cards = []
            for row in cursor:
                card = Card(row[0], row[1], row[2], row[3], row[4], row[5])
                cards.append(card)
            return cards

    def get_card_by_id(self, collection_id, location_id, card_id):
        with self.connection.cursor() as cursor:
            cursor.execute(self.get_card_by_id_query, (collection_id, location_id, card_id))
            row = cursor.fetchone()
            card = Card(row[0], row[1], row[2], row[3], row[4], row[5])
            return card

    def get_card_by_name(self, collection_id, location_id, name):
        with self.connection.cursor() as cursor:
            cursor.execute(self.get_card_by_name_query, (collection_id, location_id, name))
            row = cursor.fetchone()
            card = Card(row[0], row[1], row[2], row[3], row[4], row[5])
            return card

    def add_card(self, collection_id, location_id, name, edition, condition, is_foil):
        with self.connection.cursor() as cursor:
            cursor.execute(self.add_card_query, (collection_id, location_id, name, edition, condition, is_foil))
            row = cursor.fetchone()
            card = Card(row[0], name, edition, condition, is_foil, location_id)
            self.connection.commit()
            return card.card_id
