num=[1,2,3,4,5]
def sum(num):
    i=0
    sum=0
    while i<len(num):
        sum=sum+num[i]
        i=i+1
    print(sum)
sum(num)