import psycopg2
from Domain.Card import Card
from Domain.Collection import Collection
from Domain.Location import Location


class DataAccess:
    def __init__(self, configuration):
        self.configuration = configuration
        host = configuration.host
        user = self.configuration.user
        password = self.configuration.password
        dbname = self.configuration.dbname
        port = self.configuration.port
        self.connectionString = f'dbname={dbname} user={user} password={password} host={host} port={port}'
        self.conn = psycopg2.connect(self.connectionString)

        self.get_collections_sql = """ SELECT * FROM collections """
        self.get_collection_by_id_sql = """ SELECT * FROM collections 
            WHERE collection_id = %s """
        self.get_collection_by_name_sql = """ SELECT * FROM collections 
            WHERE name = %s """
        self.insert_collection_sql = """ INSERT INTO collections(collection_name) 
            VALUES(%s) RETURNING collection_id; """

        self.get_locations_sql = """ SELECT * FROM locations 
            WHERE collection_id = %s """
        self.get_location_by_id_sql = """ SELECT * FROM locations 
            WHERE location_id = %s """
        self.get_location_by_name_sql = """ SELECT * FROM locations 
            WHERE collection_id = %s AND name = %s """
        self.insert_location_sql = """ INSERT INTO locations(collection_id, name, description) 
            VALUES(%s, %s, %s) RETURNING location_id; """

        self.insert_card_sql = """ INSERT INTO cards(collection_id, location_id, name, edition, condition, is_foil)
             VALUES(%s, %s, %s, %s, %s, %s) RETURNING card_id; """
        self.select_cards_sql = """ SELECT * FROM cards 
            WHERE collection_id = %s AND location_id = %s """
        self.select_card_sql = """ SELECT * FROM cards 
            WHERE collection_id = %s AND location_id = %s and card_id = %s """

    def get_collections(self):
        collections = None
        with self.conn.cursor() as cur:
            cur.execute(self.get_collections_sql)
            raw_collections = cur.fetchall()
            for row in raw_collections:
                collection = Collection()
                collection.collection_id = row['collection_id']
                collection.name = row['name']
                collections.append(collection)
        return collections

    def get_collection_by_id(self, collection_id):
        collection = None
        with self.conn.cursor() as cur:
            cur.execute(self.get_collection_by_name_sql, collection_id)
            result = cur.fetchone()
            if result is not None:
                collection = Collection()
                collection.collection_id = result['collection_id']
                collection.name = result['name']
        return collection

    def get_collection_by_name(self, collection_name):
        collection = None
        with self.conn.cursor() as cur:
            cur.execute(self.get_collection_by_id_sql, collection_name)
            result = cur.fetchone()
            if result is not None:
                collection = Collection()
                collection.collection_id = result['collection_id']
                collection.name = result['name']
        return collection

    def add_collection(self, collection_name):
        collection_id = None
        with self.conn.cursor() as cur:
            cur.execute(self.insert_collection_sql, collection_name)
            collection_id = cur.fetchone()['card_id']
            self.conn.commit()
        return collection_id

    def get_locations(self, collection_id):
        locations = None
        with self.conn.cursor() as cur:
            cur.execute(self.get_locations_sql, collection_id)
            raw_locations = cur.fetchall()
            for row in raw_locations:
                location = Location()
                location.location_id = row['location_id']
                location.collection_id = row['collection_id']
                location.name = row['name']
                location.description = row['description']
                locations.append(location)
        return locations

    def get_location_by_id(self, location_id):
        location = None
        with self.conn.cursor() as cur:
            cur.execute(self.get_location_by_id_sql, location_id)
            result = cur.fetchone()
            if result is not None:
                location = Location()
                location.collection_id = result['collection_id']
                location.location_id = result['location_id']
                location.name = result['name']
                location.description = result['description']
        return location

    def get_location_by_name(self, collection_id, location_name):
        location = None
        with self.conn.cursor() as cur:
            cur.execute(self.get_location_by_name_sql, (collection_id, location_name))
            result = cur.fetchone()
            if result is not None:
                location = Location()
                location.collection_id = result['collection_id']
                location.location_id = result['location_id']
                location.name = result['name']
                location.description = result['description']
        return location

    def add_location(self, collection_id, location_name, location_description):
        location_id = None
        with self.conn.cursor() as cur:
            cur.execute(self.insert_card_sql, (collection_id, location_name, location_description))
            location_id = cur.fetchone()['location_id']
            self.conn.commit()
        return location_id

    def get_cards(self, collection_id, location_id):
        cards = None
        with self.conn.cursor() as cur:
            cur.execute(self.select_cards_sql, (collection_id, location_id))
            raw_cards = cur.fetchall()
            for row in raw_cards:
                card = Card()
                card.id = row['card_id']
                card.collection_id = row['collection_id']
                card.location_id = row['location_id']
                card.name = row['name']
                card.condition = row['condition']
                card.edition = row['edition']
                card.is_foil = row['is_foil']
                cards.append(card)
        return cards

    def get_card(self, collection_id, location_id, card_id):
        card = None
        with self.conn.cursor() as cur:
            cur.execute(self.select_card_sql, (collection_id, location_id, card_id))
            result = cur.fetchone()
            if result is not None:
                card = Card()
                card.id = result['card_id']
                card.collection_id = result['collection_id']
                card.location_id = result['location_id']
                card.name = result['name']
                card.condition = result['condition']
                card.edition = result['edition']
                card.is_foil = result['is_foil']
        return card

    def insert_card(self, collection_id, location_id, card):
        card_id = None
        with self.conn.cursor() as cur:
            cur.execute(self.insert_card_sql, (collection_id, location_id, card.name,
                                               card.edition, card.condition, card.is_foil))
            card_id = cur.fetchone()['card_id']
            self.conn.commit()
        return card_id
