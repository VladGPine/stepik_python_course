def update_dictionary(d, key, value):
    if key in d:
        d.setdefault(key, [])
        d[key].append(value)
    elif 2 * key in d:
        d[2 * key].append(value)
    else:
        d.setdefault(2 * key, [])
        d[2 * key].append(value)


d = {}
update_dictionary(d, 1, -1)
print(d)
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)