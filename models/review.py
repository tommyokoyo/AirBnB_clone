#!/usr/bin/python3
"""
    Defines the Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        Describes the Review class
        Attributes:
                place_id: (str)
                user_id: (str)
                text: (str)
    """

    place_id = ""
    user_id = ""
    text = ""
