#!/usr/bin/python3
'''
File Storage
'''
import json
from models.base_model import BaseModel


class FileStorage:
    '''
    Serializes and deserialzes json files
    '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''
        Return dictionary of <class>.<id> : object instance
        '''
        return self.__objects

    def new(self, obj):
        '''
        Add new obj to existing dictionary of instances
        '''
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        '''
        Save obj dictionaries to json file
        '''
        my_dict = {}
        if self.__objects:
            for key, value in self.__objects.items():
                my_dict[key] = value.to_dict()
            with open(self.__file_path, 'w') as f:
                json.dump(my_dict, f)

    def reload(self):
        '''
        If json file exists, convert obj dicts back to instances
        '''
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, value in new_obj.items():
                name = value['__class__']
                self.__objects[key] = eval(name)(**value)
        except FileNotFoundError:
            pass
