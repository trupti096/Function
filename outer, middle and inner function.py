#Nested Function
def outer(a):
    def middle(b):
        def inner(c):
            print(a+b+c)
        inner(6) 
    middle(5)
outer(7)

#return
def sum(a,b):
    a=8
    b=4
    c=a+b
    return c
a=5
b=6
print(sum(5,5))
