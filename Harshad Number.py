#HARSHAD NUMBER
num=int(input("enter a no="))
def function(num):
    i=1
    sum=0
    while i>0:
        r=i%10
        sum=sum+r
        i=i//10
        if num%sum==0:
            print("it is a harsad no")
        else:
            print("it is not a harsad no")
    i=i+1
function(num)
