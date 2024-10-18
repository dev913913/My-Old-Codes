from typing import Counter


for i in range (1,10):
    print(i)
    if(i==4):
        break
for i in range(1,10):
    print(i)
    if(i==5):
        continue 
tuple=["apple","mango","cherry"]
print(tuple)
num=[1,2,3,2,3,2,5,6,2,4,6]
count=num.count(2)
print("the count is",count)
l=[1,2,1,2,3,4,2,11,1,1,]
x=2
d=Counter(l)
print('{}has occured {}times'.format(x,d[x]))
list=["mon","tue","wed","thu","mon"]
elem="mon"
print("given list:\n",list)
print("given element:\n",elem)
d=Counter(list)
print("number of element present in th list:\n",d[elem])















    

    

    



    



















     








    