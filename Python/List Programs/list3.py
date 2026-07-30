list_1=[10,25,7,1,20,30,40,50,60,100,11]
count=0
for i in range(0,len(list_1)):
    if i%2 ==0:
        count=count+1
odd=len(list_1)-count
print(f"The number of even elements in {list_1} = {count}")
print(f"The number of odd elements in {list_1} = {odd}")