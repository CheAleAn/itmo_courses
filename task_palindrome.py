def is_palindrome(s):
    s = str(s)
    s = s.lower()
    lst = list(filter(lambda s: s.isalnum(), list(s)))
    return bool(lst[::] == lst[::-1])
