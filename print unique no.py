list=[1,2,3,3,3,3,4,5]
def function(list):
    i=0
    b=[]
    while i<len(list):
        if list[i] not in b:
            b.append(list[i])
        i=i+1
    print(b)
function(list)