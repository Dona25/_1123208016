list_1=[10,25,7,1,20,30,40,50,60,100,11]
max=list_1[0]
for i in range(0,len(list_1)):
    if max< list_1[i]:
        max=list_1[i]
print(f"The largest number in {list_1} = {max}")