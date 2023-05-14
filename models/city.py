#!/usr/bin/python3
"""Define City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Rep city.
    Attributes:
        state_id (str): state id.
        name (str): city name.
    """

    state_id = ""
    name = ""
