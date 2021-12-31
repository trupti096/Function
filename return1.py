list=[15,60,9,30,35,27,45]
i=0
a=[]
b=[]
c=[]
while i<len(list):
    if list[i]%3==0:
        a.append(list[i])
    if list[i]%5==0:
        b.append(list[i])
    if list[i]%3==0 and list[i]%5==0:
        c.append(list[i])
    i=i+1
print(a)
print(b)
print(c)