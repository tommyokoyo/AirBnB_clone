#!/usr/bin/python3
"""
Defines all common attributes/methods for other classes
"""
from uuid import uuid4
import datetime
import models


class BaseModel:
    """ Base Model of the project """

    def __init__(self, *args, **kwargs):
        """ Initialize a new BaseModel
            Args:
                *args (any): Tuple
                **kwargs (dict): Take in a key/value pair
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for m, n in kwargs.items():
                if m == '__class__':
                    continue
                elif m == "created_at":
                    n = datetime.datetime.strptime(n, time_format)
                elif m == "updated_at":
                    n = datetime.datetime.strptime(n, time_format)
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, m, n)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.today()
            self.updated_at = datetime.datetime.today()
            models.storage.new(self)

    def __str__(self) -> str:
        """ Returns str representation of the Basemodel Instance"""
        clsName = self.__class__.__name__
        return "[{}] ({}) {}".format(clsName, self.id, self.__dict__)

    def save(self): 
        """Updates the attribute updatedAt with current datetime"""
        self.updated_at = datetime.datetime.today()
        models.storage.save()

    def to_dict(self) -> dict:
        """ Returns a dict containing key/values of __dict__ instance"""
        instanceDict = self.__dict__.copy()
        instanceDict["__class__"] = self.__class__.__name__
        instanceDict["created_at"] = self.created_at.isoformat()
        instanceDict["updated_at"] = self.updated_at.isoformat()

        return instanceDict
