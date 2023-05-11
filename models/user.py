#!/usr/bin/python3
"""Defines the User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.
    	user's email, password, first name and last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
