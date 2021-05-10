from collections import namedtuple

def return_namedtuple(*many_names):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, tuple):
                return result
            else:
                final = namedtuple(func.__name__, list(many_names))
                return final._make(list(result))
        return wrapper
    return decorator
