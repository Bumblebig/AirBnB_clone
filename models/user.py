#!/usr/bin/python3
"""Defines User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.
    Attributes:
        email (str): user email.
        password (str): user password.
        first_name (str): user first name.
        last_name (str): user last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
