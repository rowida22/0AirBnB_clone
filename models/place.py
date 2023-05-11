#!/usr/bin/python3
"""Defines the Place class."""

from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place with the city id, user id, 
    	name,description, No.of rooms of the place, No.of bathrooms of the place
    	maximum No.of guests of the place, price by night of the place
    	latitude of the place, longitude of the place, list of amenity ids."""
    

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
