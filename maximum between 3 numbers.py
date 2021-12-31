#print
def function(num1,num2,num3):
    if num1>num2>num3:
        print(num1,"bada hai")
    elif num2>num1>num3:
        print(num2,"bada hai")
    elif num3>num2>num1:
        print(num3,"bada hai")
function(68,32,24)

#return
def function(num1,num2,num3):
    if num1>num2>num3:
        return num1,"bada hai"
    elif num2>num1>num3:
        return num2,"bada hai"
    elif num3>num2>num1:
        return num3,"bada hai"
print(function(68,32,24))
