num1=int(input("enter_1st_no="))
num2=int(input("enter_2nd_no="))
num3=int(input("enter_3rd_no="))
def number(enter_1st_no,enter_2nd_no,enter_3rd_no):
    i=1
    count=0
    sum=0
    while i<=num1:
        sum=sum+i
        count=count+1
        average=sum/count
        i=i+1
    print(sum)
    print(average)
number(num1,num2,num3)