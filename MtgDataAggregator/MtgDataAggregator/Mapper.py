from Models.Collection import Collection as ModelCollection
from Domain.Collection import Collection as DomainCollection
from Models.Location import Location as ModelLocation
from Domain.Location import Location as DomainLocation
from Models.Card import Card as ModelCard
from Domain.Card import Card as DomainCard


def map_domain_collection_list_to_model_collections_list(domain_collection_list):
    mapped_model_collection_list = None
    for domain_collection in domain_collection_list:
        mapped_model_collection = map_domain_collection_to_model_collection(domain_collection)
        mapped_model_collection_list.append(mapped_model_collection)
    return mapped_model_collection_list


def map_domain_collection_to_model_collection(domain_collection):
    mapped_model_collection = ModelCollection()
    mapped_model_collection.collection_id = domain_collection.collection_id
    mapped_model_collection.name = domain_collection.name
    return mapped_model_collection


def map_model_collection_to_domain_collection(model_collection):
    mapped_domain_collection = DomainCollection()
    mapped_domain_collection.name = model_collection.name
    return mapped_domain_collection


def map_domain_location_list_to_model_location_list(domain_location_list):
    mapped_model_location_list = None
    for domain_location in domain_location_list:
        mapped_model_location = map_domain_location_to_model_location(domain_location)
        mapped_model_location_list.append(mapped_model_location)
    return mapped_model_location_list


def map_domain_location_to_model_location(domain_location):
    mapped_model_location = ModelLocation()
    mapped_model_location.location_id = domain_location.location_id
    mapped_model_location.name = domain_location.name
    mapped_model_location.descriptions = domain_location.descriptions
    return mapped_model_location


def map_model_location_to_domain_location(model_location, collection_id):
    mapped_domain_location = DomainLocation()
    mapped_domain_location.collection_id = collection_id
    mapped_domain_location.location_id = model_location.location_id
    mapped_domain_location.name = model_location.name
    mapped_domain_location.description = model_location.description
    return mapped_domain_location


def map_domain_card_list_to_model_card_list(domain_card_list):
    mapped_model_card_list = None
    for domain_card in domain_card_list:
        mapped_model_card = map_domain_card_to_model_card(domain_card)
        mapped_model_card_list.append(mapped_model_card)
    return mapped_model_card_list


def map_domain_card_to_model_card(domain_card):
    mapped_model_card = ModelCard()
    mapped_model_card.card_id = domain_card.card_id
    mapped_model_card.name = domain_card.name
    mapped_model_card.edition = domain_card.edition
    mapped_model_card.is_foil = domain_card.is_foil
    return mapped_model_card


def map_model_card_to_domain_card(model_card, collection_id, location_id):
    mapped_domain_card = DomainCard()
    mapped_domain_card.card_id = model_card.card_id
    mapped_domain_card.collection_id = collection_id
    mapped_domain_card.location_id = location_id
    mapped_domain_card.edition = model_card.edition
    mapped_domain_card.condition = model_card.condition
    mapped_domain_card.is_foil = model_card.is_foil
    return mapped_domain_card



