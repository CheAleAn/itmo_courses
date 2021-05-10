from abc import ABCMeta, abstractmethod
import pickle
import json
import os

class ParamHandlerException(Exception):
    def __init__(self, *args, **kwargs):
        pass


class ParamHandler(metaclass=ABCMeta):
    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value

    def get_param(self, key):
        return self.params.get(key)

    def get_all_params(self):
        return self.params

    def remove_param(self, key):
        self.params.pop(key)

    def remove_all_params(self):
        self.params.clear()

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


class ParamHandlerFactory(object):
    types = {}

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name.')

        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException(f'Class "{klass}" is not ParamHandler.')
        cls.types[name] = klass

    @classmethod
    def create(cls, source):
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)
        if klass is None:
            raise ParamHandlerException(f'Type "{ext}" not found.')
        return klass(source)


class JsonParamHandler(ParamHandler):
    def read(self):
        """Чтение в формате Json и присвоение значений в self.params"""
        with open(self.source) as s:
            self.params = json.load(s)

    def write(self):
        """Запись в формате Json параметров self.params"""
        with open(self.source, 'w') as s:
            json.dump(self.params, s, indent=4)


class PickleParamHandler(ParamHandler):
    def read(self):
        """Чтение в формате Pickle и присвоение значений в self.params"""
        with open(self.source, 'rb') as s:
            self.params = pickle.load(s)

    def write(self):
        """Запись в формате Pickle параметров self.params"""
        with open(self.source, 'wb') as s:
            pickle.dump(self.params, s)


ParamHandlerFactory.add_type('json', JsonParamHandler)
ParamHandlerFactory.add_type('pickle', PickleParamHandler)
