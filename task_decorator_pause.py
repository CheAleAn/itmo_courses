import time

def pause(kek):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(kek)
            return func(*args, **kwargs)
        return wrapper
    return decorator
