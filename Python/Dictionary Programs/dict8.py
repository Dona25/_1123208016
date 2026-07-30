d = {"a": 3, "b": 1, "c": 2}
sorted_dict = {}
values = sorted(d.values())
for value in values:
    for key in d:
        if d[key] == value and key not in sorted_dict:
            sorted_dict[key] = value
            break
print(sorted_dict)