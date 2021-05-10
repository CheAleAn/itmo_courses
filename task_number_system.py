def function_to_10(number, const):
    number = str(number)
    lst = list(filter(lambda number: number.isalnum(), list(number)))
    k = 0
    for i in range(0, len(lst)):
        lst[i] = lst[i].replace('a','10')
        lst[i] = lst[i].replace('b','11')
        lst[i] = lst[i].replace('c','12')
        lst[i] = lst[i].replace('d','13')
        lst[i] = lst[i].replace('e','14')
        lst[i] = lst[i].replace('f','15')

    for i in range(0, len(lst)):
        k += const ** i *  int(lst[len(lst) - 1 - i])

    return k

def bin2dec(number):
    return function_to_10(number, 2)

def oct2dec(number):
    return function_to_10(number, 8)

def hex2dec(number):
    return function_to_10(number, 16)

def func_from_10(number, const):
    lst = []
    while number / const:
        lst += [number % const] #list.append(number % const)
        number = number // const

    for i in range(0, len(lst)):
        if lst[i] == 10:
            lst[i] = 'a'
        elif lst[i] == 11:
            lst[i] = 'b'
        elif lst[i] == 12:
            lst[i] = 'c'
        elif lst[i] == 13:
            lst[i] = 'd'
        elif lst[i] == 14:
            lst[i] = 'e'
        elif lst[i] == 15:
            lst[i] = 'f'
    for i in range(0, len(lst)):
        lst[i] = str(lst[i])
    lst = lst[::-1]
    return ''.join(lst)

def dec2bin(number):
    return func_from_10(number, 2)

def dec2oct(number):
    return func_from_10(number, 8)

def dec2hex(number):
    return func_from_10(number, 16)
