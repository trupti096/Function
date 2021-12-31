#print
string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
def list(string_list):
    i=0
    b=[]
    while i<len(string_list):
        j=0
        while j<len(string_list):
            if string_list[i] not in b:
                b.append(string_list[i])
            j=j+1
        i=i+1
    print(b)
list(string_list)

#return
string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
def list(string_list):
    i=0
    b=[]
    while i<len(string_list):
        j=0
        while j<len(string_list):
            if string_list[i] not in b:
                b.append(string_list[i])
            j=j+1
        i=i+1
    return b
print(list(string_list))
