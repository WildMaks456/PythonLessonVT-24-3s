def flatten_dict(d,parent_key ="", sep="_"):
    result = {}
    for key, value in d.items():
        new_key = parent_key +sep +key if parent_key else key
        if isinstance(value, dict):
            result.update(flatten_dict(value, new_key<sep))
        else:
            result[new_key]=value
    return result

print(flatten_dict({"a":{"b": 1, "c": 2}, "d":3}))
#{'a_b':1, 'a_c':2, 'd':3}