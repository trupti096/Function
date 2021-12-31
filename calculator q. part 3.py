
def list_change(list1,list2):
    i=0
    b=[]
    while i<len(list1):
        m=list1[i]*list2[i]
        b.append(m)
        i=i+1
    print(b)
list_change([5, 10, 50, 20],[2, 20, 3, 5])
