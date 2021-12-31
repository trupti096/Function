num=int(input("eter a no="))
def showNumbers(limit):
    i=0
    while i<=num:
        if i%2==0:
            print(i,"even no")
        elif i%2!=0:
            print(i,"odd no")
        i=i+1
showNumbers(num)