list=[6,8,4,3,9,56,0,34,7,15]
def sort(list):
    i=0
    b=[]
    while i<len(list):
        j=0
        while j<len(list):
            if list[i]<list[j]:
                list[i],list[j]=list[j],list[i]
            j=j+1
        i=i+1
    print(list)
sort(list)