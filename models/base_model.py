#!/usr/bin/python3
"""
Defines all common attributes/methods for other classes
"""
from uuid import uuid4
import datetime


class BaseModel:
    """ Base Model of the project """

    def __init__(self, *args, **kwargs):
        """ Initialize a new BaseModel
            Args:
                *args (any): Tuple
                **kwargs (dict): Take in a key/value pair
        """
        self.id = str(uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for m, n in kwargs.items():
                if m == "created_at" or m == "updated_at":
                    self.__dict__[m] = datetime.datetime.strptime(n, time_format)
                else:
                    self.__dict__[m] = n

    def __str__(self) -> str:
        """ Returns str representation of the Basemodel Instance"""
        clsName = self.__class__.__name__
        return "[{}] ({}) {}".format(clsName, self.id, self.__dict__)

    def save(self): 
        """Updates the attribute updatedAt with current datetime"""
        self.updated_at = datetime.datetime.today()

    def to_dict(self) -> dict:
        """ Returns a dict containing key/values of __dict__ instance"""
        instanceDict = self.__dict__.copy()
        instanceDict["__class__"] = self.__class__.__name__
        instanceDict["created_at"] = self.created_at.isoformat()
        instanceDict["updated_at"] = self.updated_at.isoformat()

        return instanceDict
