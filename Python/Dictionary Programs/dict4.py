text = input("Enter a string: ")
d = {}
for ch in text:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
print(d)