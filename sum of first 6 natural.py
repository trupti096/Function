#print
def sum(n):
    i=0
    add=0
    while i<=n:
        add=add+i
        i=i+1
    print(add)
sum(6)


#return
def sum(n):
    i=0
    a=0
    while i<=n:
        a=a+i
        i=i+1
    return a
print(sum(6))