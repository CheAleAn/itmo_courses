class MoneyArithmeticError(ArithmeticError):
    def __init__(self):
        return super().__init__()
    def warning(self):
        raise OperandTypeError("The coefficient should be positive")


class OperandTypeError(TypeError):
    def __init__(self):
        return super().__init__(self)
    def warning(a,b):
        raise OperandTypeError(f"unsupported operand type(s) for {a}: 'Money' and '{b}'")


class Money(object):
    def __init__(self, whole, fraction=0):
        self.x = whole if whole else fraction // 100
        self.y = fraction if whole else fraction % 100

    def get_whole(self):
        return self.x

    def get_fraction(self):
        return self.y

    def __repr__(self):
        return f'{__class__.__name__}({self.x}, {self.y:02})'

    def __add__(self, other):
        """ Перегрузка + """
        if isinstance(other, Money):
            return self.__class__(((self.x + other.x)*100 + self.y + other.y) // 100, ((self.x + other.x)*100 + self.y + other.y) % 100)
        else:
            OperandTypeError.warning('+', type(other))

    def __sub__(self, other):
        """ Перегрузка - """
        try:
            return self.__class__(((self.x - other.x)*100 + self.y - other.y) // 100, ((self.x - other.x)*100 + self.y - other.y) % 100)
        except:
            OperandTypeError.error('-', type(other))

    def __mul__(self, other):
        """ Перегрузка * """
        try:
            return self.__class__(((self.x*100 + self.y) * other) // 100, ((self.x*100 + self.y) * other) % 100)
        except:
            OperandTypeError.error('*', type(other))

    def __mul__(self, other):
        """ Перегрузка * """
        try:
            return self.__class__(((self.x*100 + self.y) * other) // 100, ((self.x*100 + self.y) * other) % 100)
        except:
            OperandTypeError.error('*', type(other))





















abc = Money(120, 10)
dfg = 10#Money(140, 30)
keyk = abc + dfg
print(keyk.get_whole(), keyk.get_fraction(), keyk)
