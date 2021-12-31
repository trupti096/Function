# Ek function define karo jo ki input me 2 strings lega aur dono strings me se 
# jiski length jyaada hogi use print karega aur agar dono strings ki length equal 
# hui to dono ko line by line print karega . Hint :- use len() builtin function.. 

def function_name(name1,name2):
    i=0
    count=0
    while i<len(name1):
        j=0
        while j<len(name1):
            count=count+1
            j=j+1
        i=i+1
    print(j)

function_name("sonu","monu")
    