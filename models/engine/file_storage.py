#!/usr/bin/python3
"""class for serializion and deserialization """
import json
import os


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[k] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        dct = {}
        for key, value in FileStorage.__objects.items():
            dct[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as fl:
            json.dump(dct, fl)

    def reload(self):
        """ Deserializes __objects from the JSON file """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review
        dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'City': City,
               'Amenity': Amenity,
               'State': State,
               'Review': Review}
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as fl:
                for key, value in json.load(fl).items():
                    self.new(dct[value['__class__']](**value)

