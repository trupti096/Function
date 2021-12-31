list = [1, 2, 3, 4, 5, 6, 7, 10, -2]

def max(list):
    i=0
    max=0
    while i<len(list):
        if list[i]>max:
            max=list[i]
        i=i+1
    print(max)
max(list)