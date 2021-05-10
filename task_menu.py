from abc import ABCMeta, abstractmethod
from collections import OrderedDict

class CommandException(Exception):
    def __init__(self, *args, **kwargs):
        pass

    __module__ = Exception.__module__


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class Menu(object):
    def __init__(self):
        self.menu = OrderedDict()
        self.counter = 0
        self.name = ''

    def add_command(self, name, klass):
        if not name:
            raise CommandException('Command must have a name')
        if not issubclass(klass, Command):
            raise CommandException(f'Class "{klass.__name__}" is not Command')

        self.menu[name] = klass

    def execute(self, name, *args, **kwargs):
        func = self.menu.get(name)
        if func is None:
            raise CommandException(f'Command with name "{name}" not found')

        return func(*args, **kwargs).execute()

    def get_size(self):
        return len(self.menu)

    def get_items(self):
        return self.menu.items()

    def __next__(self):
        dict_size = self.get_size()
        menu_items = list(self.get_items())
        if self.counter < dict_size:
            number = self.counter
            self.counter += 1
            return menu_items[number]
        else:
            raise StopIteration

    def __iter__(self):
        return self
