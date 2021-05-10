from abc import ABCMeta, abstractmethod
from datetime import datetime

class Validator(metaclass=ABCMeta):
    @abstractmethod
    def validate(self, value):
        pass


class DateTimeValidator(Validator):
    def __init__(self, date_formats=[]):
        self.date_formats = date_formats
        self.date = None

    def validate(self, value):
        if not self.date_formats:#если не заданы форматы
            self.years = ['%Y-%m-%d', '%d.%m.%Y', '%d/%m/%Y']
            self.hours = ['', ' %H:%M', ' %H:%M:%S']
            for i in self.years:
                for j in self.hours:
                    self.date_formats.append(i + j)

        for i in self.date_formats:
            try:
                self.date = datetime.strptime(value, i)
                #если подойдет по формату, то запишет результат разборки строки
            except:
                pass

        return self.date is not None
        #была ли в итоге успешная разборка строки (подошел ли хоть один формат)


class EMailValidator(Validator):
    def validate(self, value):
        first_check = bool(value.find('@', 1, len(value) - 1) > 0)
        #есть знак @ между первым и последним символами
        second_check = bool(value.find('@') == value.rfind('@'))
        #знак @ встречается единожды
        return (first_check & second_check)


class ChainValidator(object):
    def __init__(self, validators):
        self.validators = validators
        self.answers = []

    def validate(self, value):
        for i in self.validators:
            self.answers.append(i.validate(value))

        for i in self.answers:
            if i is False:
                return i

        return True
