#print
sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
def break_into_words(setence):
    i=0
    while i<len(sentence):
        x=sentence.split()
        i=i+1
    print(x)
break_into_words(sentence)

#return
sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
def break_into_words(setence):
    i=0
    while i<len(sentence):
        x=sentence.split()
        i=i+1
    return x
print(break_into_words(sentence))