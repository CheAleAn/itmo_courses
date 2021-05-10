def geometric_progression_generator(b, q):
    if not b:
        raise ArithmeticError("The first term is zero")
    elif not q:
        raise ArithmeticError("The denominator is zero")
    else:
        yield b
        while 1:
            b *= q
            yield b
