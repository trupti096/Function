list = [8, 6, 4, 8, 4, 50, 2, 7]
def min(list):
    i=0
    min=0
    while i<len(list):
        if list[i]<min:
            list[i]=min
        i=i+1
    print(i)
min(list)