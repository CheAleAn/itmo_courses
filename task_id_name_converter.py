def snake_to_camel(name):
    name = name.title()
    lst = name.split('_')
    s = ''
    return s.join(lst)

def camel_to_snake(name):
    data = list(name)
    for i in range(1, len(data)):
        if 'A' <= data[i] <= 'Z':
            data[i] = '_'+ ''.join(data[i])
    str = ''.join(data)
    return str.lower()
