#!/usr/bin/python3
""" A base class that takes argument int values, increments if no values
    are given.
"""
import json

class Base:
    """ Creates the class base with id arguments. """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string =="":
            return []
        return json.loads(json_string)
    
    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r") as file:
                json_string = file.read()
                dict_list = Base.from_json_string(json_string)
                return [cls.create(**dict_obj) for dict_obj in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a dummy instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a dummy instance
        else:
            return None

        dummy_instance.update(**dictionary)  # Update dummy instance with real values
        return dummy_instance
