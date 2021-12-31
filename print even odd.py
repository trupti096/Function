a=[2, 6, 18, 10, 3, 75]
b=[6, 19, 24, 12, 3, 87] 
def check_numbers_list(a,b):
    i=0
    while i<len(a):
        if a[i]%2==0 and b[i]%2==0:
            print("dono even number hai")
        else:
            print("dono odd number hai")
        i=i+1
check_numbers_list(a,b)