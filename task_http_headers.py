def http_headers_to_json(address1, address2):
    import json
    with open(address1) as file:
        lst = file.readlines()

    if not lst[len(lst)-1].isalnum():
        lst.pop()

    for i in range(len(lst)):
        lst[i] = lst[i].strip()

    data = []
    for i in lst[0].split():
        data.append(i)

    if data[0].count("HTTP/2"):
        keys = ['protocol', 'status_code']
    elif data[0].count("HTTP/1.0") or data[0].count("HTTP/1.1"):
        while len(data) > 3:
            data[2] = ' '.join([data[2], data.pop()])
        keys = ['protocol', 'status_code', 'status_message']
    else:
        keys = ['method', 'uri', 'protocol']

    for i in range(1, len(lst)):
        symbol = lst[i].find(':')
        keys.append(lst[i][0: symbol])
        data.append(lst[i][symbol + 2: len(lst[i])])

    result = dict.fromkeys(keys)
    for i in range(len(keys)):
        if type(result[keys[i]]) == list:
            result[keys[i]].append(data[i])
        elif type(result[keys[i]]) == str:
            temp = []
            temp.append(result[keys[i]])
            temp.append(data[i])
            result[keys[i]] = temp
        else:
            result[keys[i]] = data[i]

    with open(address2, 'w') as f:
        json.dump(result, f)
