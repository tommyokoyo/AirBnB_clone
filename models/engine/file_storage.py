#!/usr/bin/python3
"""
    This Class serializes instances to a JSON file
    and deserializes JSON file to instances
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
        Defines the storage engine
        attributes:
                    __file_path: (string) path to the JSON file
                    __objects: (dict)stores all objects by <class.name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            return the dict objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
        """
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """
            serializes __objects to the JSON file
        """
        new_dict = {key: obj.to_dict() for key, obj in
                    FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as filename:
            json.dump(new_dict, filename)

    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r',
                      encoding='utf-8') as filename:
                loaded_file = json.load(filename)
                for key, value in loaded_file.items():
                    FileStorage.__objects[key] = eval(
                        value['__class__'])(**value)
