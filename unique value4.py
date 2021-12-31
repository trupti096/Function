# Socho aapke paas 2 lists hain. Aapne aisa code likhna hain jisse ek nayi list 
# banne jisme inn dono lists ke woh item hone chaiye ho dono list mein aa rahe hain. 
# Socho aapki do list yeh hain:


#print
list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
def function(list1,list2):
    i=0
    b=[]
    c=list(list1)
    d=list(list2)
    while i<len(list1):
        if c[i] in d:
            if c[i] not in b:
                b.append(c[i])
        i=i+1
    print(b)
function(list1,list2)

#return
list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
def function(list1,list2):
    i=0
    b=[]
    c=list(list1)
    d=list(list2)
    while i<len(list1):
        if c[i] in d:
            if c[i] not in b:
                b.append(c[i])
        i=i+1
    return b
print(function(list1,list2))