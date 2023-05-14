#!/usr/bin/python3
"""Defines State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Rep a state.
    Attributes:
        name (str): name of state.
    """

    name = ""
