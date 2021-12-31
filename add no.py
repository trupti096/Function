#positional arguments
def sum(a,b):
    c=a+b
    print(c)
sum(5,5)


#keyword arguments
def sum(a=4,b=8):
    c=a+b
    print(c)
sum(5,b=5)


#default arguments
def my(a,b=10):
    c=a+b
    print(c)
my(2,5)
