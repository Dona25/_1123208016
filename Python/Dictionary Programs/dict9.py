d = {"a": 1, "b": 2, "c": 3}
new = {}
for key, value in d.items():
    new[value] = key
print(new)