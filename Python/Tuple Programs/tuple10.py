t = (1, 2, 2, 3, 4, 4, 5)
new_tuple = ()
for i in t:
    if i not in new_tuple:
        new_tuple += (i,)
print(new_tuple)