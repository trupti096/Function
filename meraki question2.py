#part1

# Apko students naam ka ek function define karna hai or uss function mai list of 
# students name as a parameter pass karna hai(List ka use nahi karna hai)

def greet(names):
    print(names)
names=("Barsha","Swarnalata","Puja","Naaz","Abhipsa")
greet(names)

#part2

# Apko isGreaterThen20 naam ka function define karna hai jismai apko 
# function mai do parameter pass karane hai or first parameter by default 20 hi hona chahiye.

def isgreaterthan20(a,b=20):
    print(a)
    print(b)
a=10
isgreaterthan20(20,a)
