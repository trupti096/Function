#1
def col(a,b):
    return a+b,a-b,a*b,a/b
a=3
b=6
print(col(a,b))

#2
def col(a,b):
    return a+b,a-b,a*b,a/b
print(col(3,6))

#3
def sum(a,b):
    a=8
    b=4
    c=a+b
    return c
a=5
b=2
print(sum(5,5))

#4
a=5
b=6
def sum(a,b):
    a=5
    b=6
    c=a+b
    return c
a=10
b=20
print(sum(25,35))
print(a,b)

#5
def call(a,b):
    c=a+b
    return c
a=5
b=6
print(call(7,8))
print(call(a,b))