class MatrixSizeError(ArithmeticError):
    def __init__(self):
        pass


class OperandTypeError(TypeError):
    def __init__(self):
        pass


class Matrix(object):
    def __init__(self, value):
        self.value = value
        self.strok = len(self.value)
        self.stolbec = len(self.value[0])
