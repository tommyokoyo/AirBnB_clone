#!/usr/bin/python3
"""
    Defines the City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        Describes a user
        Attributes:
                state_id: (str)
                name: (str)
    """

    state_id = ""
    name = ""
