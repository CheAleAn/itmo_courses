import hashlib


def make_token(username, password):
    s = username + password
    return hashlib.md5(s.encode()).hexdigest()


cache = {
'logined': 0
}

def login_required(func):
    def wrapper(*args, **kwargs):
        if cache['logined']:
            return func(*args, **kwargs)
        else:
            with open('token.txt') as t:
                origin_sum = t.read()
            for i in range(3):
                login = input()
                password = input()
                checking_sum = make_token(login, password)
                if checking_sum == origin_sum:
                    cache['logined'] = 1
                    return func(*args, **kwargs)

            raise RuntimeError('Authentication failed')

    return wrapper
