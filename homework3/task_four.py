from collections import defaultdict
dict_a = {'a': 1, 'b': 2, 'c': 3}
dict_b = {'c': 3, 'd': 4, 'e': 5}
dict_ab = defaultdict(list)
for key in sorted(set(list(dict_a.keys()) + list(dict_b.keys()))):
    if key in dict_a:
        dict_ab[key].append(dict_a[key])
        if key not in dict_b:
            dict_ab[key].append(None)
    if key in dict_b:
        if key not in dict_a:
            dict_ab[key].append(None)
        dict_ab[key].append(dict_b[key])
print(f"ab = {dict(dict_ab)}")
