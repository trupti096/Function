#print
def function(factorial):
    num=int(input("enter a no="))
    i=1
    while num>0:
        i=i*num
        num=num-1
    print("factorial=",i)
function(7)

#return
def function(factorial):
    num=int(input("enter a no="))
    i=1
    while num>0:
        i=i*num
        num=num-1
    return "factorial=",i
print(function(7))