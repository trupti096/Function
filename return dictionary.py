def function(num):
    dictionary={}
    i=1
    while i<=num:
        dictionary[i]=i**2
        i=i+1
    return dictionary
print(function(20))