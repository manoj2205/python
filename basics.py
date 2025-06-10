
import sys
import math
import random
import threading
import time
from functools import reduce

# ----- INTRO -----
# Python files end with the extension .py
# Print to the console
# Python statements terminate with a newline
print("Hello World")

# Accept user input and store it in a variable
# name = input("What is your name ")
# print("Hi ", name)

# If you want to extend a statement to multiple
# lines you can use parentheses or \
v1 = (
        1 + 2
        + 3
)
v1 = 1 + 2 \
     + 3

# Put multiple statements on 1 line
v1 = 5;
v1 = v1 - 1

"""
Multi-line
Comment
"""

# ----- VARIABLES -----
# Variables are names assigned to values
# The 1st character must be _ or a letter
# Then you can use letters, numbers or _
# Variable names are type sensitive
v2 = 1
V2 = 2  # v1 is different from V1

# You can assign multiple variables
v3 = v4 = 20

# ----- DATA TYPES -----
# Data in Python is dynamically typed and that
# data type can change
# All data is an object which I cover later
# The basic types are integers, floats,
# complex numbers, strings, booleans
# Python doesn't have a character type

# How to get the type
print(type(10))

# There is no limit to the size of integers
# This is a way to get a practical max size
print(sys.maxsize)

# Floats are values with decimal values
# This is how to get a max float
print(sys.float_info.max)

# But, they are accurate to 15 digits
f1 = 1.1111111111111111
f2 = 1.1111111111111111
f3 = f1 + f2
print(f3)

# Complex numbers are [real part]+[imaginary part]
cn1 = 5 + 6j

# Booleans are either True or False
b1 = True

# Strings are surrounded by ' or "
str1 = "Escape Sequences \' \t \" \\ and \n"

str2 = '''Triple quoted strings can contain ' and "'''

# You can cast to different types with int, float,
# str, chr
print("Cast ", type(int(5.4)))  # to int
print("Cast 2 ", type(str(5.4)))  # to string
print("Cast 3 ", type(chr(97)))  # to string
print("Cast 4 ", type(ord('a')))  # to int

# ----- OUTPUT -----
# You can define a separator for print
print(12, 21, 1974, sep='/')

# Eliminate newline
print("No Newline", end='')

# String formatting %e for exponent
print("\n%04d %s %.2f %c" % (1, "Derek", 1.234, 'A'))

# ----- MATH -----
print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)
print("5 % 2 =", 5 % 2)
print("5 ** 2 =", 5 ** 2)
print("5 // 2 =", 5 // 2)

# Shortcuts
i1 = 2
i1 += 1
print("i1 ", i1)

# Math Functions
print("abs(-1) ", abs(-1))
print("max(5, 4) ", max(5, 4))
print("min(5, 4) ", min(5, 4))
print("pow(2, 2) ", pow(2, 2))
print("ceil(4.5) ", math.ceil(4.5))
print("floor(4.5) ", math.floor(4.5))
print("round(4.5) ", round(4.5))
print("exp(1) ", math.exp(1))  # e**x
print("log(e) ", math.log(math.exp(1)))
print("log(100) ", math.log(100, 10))  # Base 10 Log
print("sqrt(100) ", math.sqrt(100))
print("sin(0) ", math.sin(0))
print("cos(0) ", math.cos(0))
print("tan(0) ", math.tan(0))
print("asin(0) ", math.asin(0))
print("acos(0) ", math.acos(0))
print("atan(0) ", math.atan(0))
print("sinh(0) ", math.sinh(0))
print("cosh(0) ", math.cosh(0))
print("tanh(0) ", math.tanh(0))
print("asinh(0) ", math.asinh(0))
print("acosh(pi) ", math.acosh(math.pi))
print("atanh(0) ", math.atanh(0))
print("hypot(0) ", math.hypot(10, 10))  # sqrt(x*x + y*y)
print("radians(0) ", math.radians(0))
print("degrees(pi) ", math.degrees(math.pi))

# Generate a random int
print("Random", random.randint(1, 101))

# ----- NaN & inf -----
# inf is infinity
print(math.inf > 0)

# NaN is used to represent a number that can't
# be defined
print(math.inf - math.inf)

# ----- CONDITIONALS -----
# Comparison Operators : < > <= >= == !=

# if, else & elif execute different code depending
# on conditions
age = 30
if age > 21:
    # Python uses indentation to define all the
    # code that executes if the above is true
    print("You can drive a tractor trailer")
elif age >= 16:
    print("You can drive a car")
else:
    print("You can't drive")

# Make more complex conditionals with logical operators
# Logical Operators : and or not
if age < 5:
    print("Stay Home")
elif (age >= 5) and (age <= 6):
    print("Kindergarten")
elif (age > 6) and (age <= 17):
    print("Grade %d", (age - 5))
else:
    print("College")

# Ternary operator in Python
# condition_true if condition else condition_false
canVote = True if age >= 18 else False

# ----- STRINGS -----
# Raw strings ignore escape sequences
print(r"I'll be ignored \n")

# Combine strings with +
print("Hello " + "You")

# Get string length
str3 = "Hello You"
print("Length ", len(str3))

# Character at index
print("1st ", str3[0])

# Last character
print("Last ", str3[-1])

# 1st 3 chrs
print("1st 3 ", str3[0:3])  # Start, up to not including

# Get every other character
print("Every Other ", str3[0:-1:2])  # Last is a step

# You can't change an index value like this
# str3[0] = "a" because strings are immutable
# (Can't Change)
# You could do this
str3 = str3.replace("Hello", "Goodbye")
print(str3)

# You could also slice front and back and replace
# what you want to change
str3 = str3[:8] + "y" + str3[9:]
print(str3)

# Test if string in string
print("you" in str3)

# Test if not in
print("you" not in str3)

# Find first index for match or -1
print("You Index ", str3.find("you"))

# Trim white space from right and left
# also lstrip and rstrip
print("    Hello    ".strip())

# Convert a list into a string and separate with
# spaces
print(" ".join(["Some", "Words"]))

# Convert string into a list with a defined separator
# or delimiter
print("A, string".split(", "))

# Formatted output with f-string
int1 = int2 = 5
print(f'{int1} + {int2} = {int1 + int2}')

# To lower and upper case
print("A String".lower())
print("A String".upper())

# Is letter or number
print("abc123".isalnum())

# Is characters
print("abc".isalpha())

# Is numbers
print("abc".isdigit())

# ----- LISTS -----
# Lists can contain mutable pieces of data of
# varying data types or even functions
l1 = [1, 3.14, "Derek", True]
print("length",len(l1))
print("first",l1[0])
print("last",l1[-1])
l1[0]=2
print(l1)
#this overwrites the existing data
l1[2:3]=["manoj","gude",12]
print(l1)
#this inserts 2 records in 2 places from the position this will not overwrite the data
l1[2:2]=["gude","kumar"]
print(l1)
l2=l1+["Egg",2]
l2.remove("manoj")
l2.pop(0)
print(l2)
l2.remove("gude")
print(l2)
#You cannot use a non-integer value (like a string) with pop() instead we can use remove()
l3 = [[1,0],[2,3]]
l4 = ['Egg',3]+l3 #l4 = ['Egg',3,[1,0],[2,3]]
print(l4[2][1]) #output - [0]
#Enumerate() - function that returns both the index and the element for each item in the list.
l4 = ['Egg', 3, [1, 0], [2, 3]]
print(l4[0:-1])# This omits the last item in the list
print(l4[0:]) # This print the all items in the list
print(l4[::-1]) #reverse string
print(1 in l4) #checking element is present in the list or not
print(l4[0:-1:2]) #list[start:stop:step]
for i, char in enumerate(l4):
    print(i, char)
#break - It terminates the loop immediately, and the program control resumes at the next statement following the loop.
for i in range(10):
    if i == 5:
        break
    print(i)
#continue - It skips the rest of the current iteration of the loop and proceeds to the next iteration.
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
#while loop
# A while loop executes the piece of code as long as a specified condition is true;
w1=5
print(w1)
while(w1>1):
    print(w1)
    w1 -=1

#printing even value
print("even value printing")
w2=0
while w2<=20:
    if w2%2==0:
        print(w2)
    elif w2 == 9:
        break
    else:
        w2+=1
        continue
    w2+=1
# Here poping the
l4 = [1,3.14,"Derek"]
while len(l4): # means the list is not empty return a number
    print(l4.pop(0)) #removes the first element and print it

#for loops - programming construct that allows a block of code to be executed repeatedly, a certain number of times.
for c in range(0,10):
    print(c,'',end='')
print(c)

l4 =[1,3.14,'Derek']
for x in l4:
    print(x)

for x in [2,4,6]:
    print(x)

#Iterator - This allow you to pass an object to a function called iterator which are iterable cycle through values.
l5=[6,9,12]
itr = iter(l5)
print(next(itr))
print(next(itr))
print(list(range(0,10,2))) #(start,end,step)
num_list = [[1,2,3],[10,20,30],[100,200,300]]
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

#Tuples - immutable 
t1=(1,3.14,"Derek")
print("Length", len(t1))
print("1st", t1[0])
print("Last",t1[-1])
print("1st 2", t1[0:2])
print("Every other", t1[0:-1:2])
print("Reverese",t1[::-1])

#Dictionaries - list of key value ppairs. key and values can use any data type. No duplicates
heroes = {
    "Superman" : "Clark Kent",
    "Batman" : "Bruce Wayne"
}

villian = dict(Lex="Luther",Loki="Loki")
print(villian)

print(len(villian))
print(heroes["Batman"])
heroes["Flash"]="Barry Allen"
heroes["Flash"]="Barry Allen"
print(list(heroes.items()))
print(list(heroes.keys()))
print(list(heroes.values()))

del heroes["Flash"]
print(heroes.pop("Batman"))
print("Superman" in heroes)
for k in heroes:
    print(k)

for v in heroes.values():
    print(v)

d1 = {"name":"Bread","price": .88} 
print("%(name)s costs $%(price).2f" % d1)


# A set is a collection which is unordered, unchangeable, and unindexed. doesn't allow duplicates
s1 = set(["Derek",1])
s2 = {"Paul", 1}

print("Length", len(s2))
s3 = s1 | s2 # joining the sets
print(s3)
s3.add("Doug")
s3.discard("Derek")
print("Poping Random", s3.pop())
s3 |= s2
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1.difference(s2))
s3.clear()
s4 = frozenset(["Paul",7]) #frozenset is just like a set, but cannot be modified (no add/remove).
print("s4",s4)

#function
def namee():
    print("manoj") #here it prints none

print(namee()) #this returns the name and none because this function doesn't return anything
namee() #this just returns name

def multiply(x,y):
    return x+y #the value next to the return will be returned

print(multiply(3,4)) #if dont keep the function inside print it will not print anything
#Function Arguments
#1)Default Arguments-  define a value for a parameter in the function definition. If the caller does not provide a value for that parameter, Python will use the default.
def greet(name, country="India"):
    print(f"Hello {name} from {country}!")

greet("Manoj")             # uses default "India"
greet("Sara", "USA")       # overrides default
#2)Positional Arguments Positional arguments are passed to a function in the order they are defined.
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Manoj", 30)

def greet(name, age):
    print(f"{name} is {age} years old.")

#greet("Manoj")  # ❌ TypeError: missing 1 required positional argument

def greet(name, age=25):  # age has default value
    print(f"{name} is {age} years old.")

greet("Manoj")  # ✔ uses default age = 25

def greet(name, age, city):
    print(f"{name}, {age}, from {city}")

greet("Manoj", 30, city="Dallas")  # ✔ OK

#In a function call, positional arguments must come before keyword arguments.
#Valid
greet("Manoj", 30, "Dallas")          # All positional
greet("Manoj", 30, city="Dallas")     # Positional first, then keyword
greet(name="Manoj", age=30, city="Dallas")  # All keyword
#Invalid
#greet(name="Manoj", 30, "Dallas")     # ❌ Keyword first, then positional

#*args - *args allows you to pass a variable number of positional arguments to a function. This treats like tuple
def add_numbers(*args):
    print(args)
    return sum(args)

print(add_numbers(1, 2, 3))  # Output: 6
print(add_numbers(10, 20))   # Output: 30

#**kwargs lets you pass a variable number of keyword arguments (name=value pairs). This treats like dictionary
def print_details(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Manoj", age=30, country="India")

def demo(a, b=2, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 5, 6, 7, 8, name="Manoj", age=30)

def get_sum2(*args):
    sum=0
    for arg in args:
        sum +=arg
    return sum
print(get_sum2(1,2,3,4))

def next_2(n):
    return n+1, n+2

i1,i2 = next_2(5)
print(i1,i2)

def yes(*args):
    return lambda x,y: x+y
add = yes(5,6)
print(add(5,6))

def mult_by(num):
    return lambda x:x*num
print("3 * 5 =", (mult_by (3)(5)))

def mult_list(list,func):
    for x in list:
        print(func(x))
mult_by_4=mult_by(4)
mult_list(list(range(0,5)), mult_by_4)
# Create list of functions
power_list = [lambda x : x**2,
              lambda x : x**3]
print(power_list)

#map - allows you to apply a function to every item in an iterable (like a list or tuple) — without writing a loop manually.
#A map object is an iterator — it holds the transformation logic, but doesn't execute it immediately.
#It’s lazy — meaning:
#It doesn’t compute all values right away.
#It generates each value only when needed.
#This is great for memory efficiency, especially with large datasets.
nums = [1, 2, 3, 4]

# Function to square a number
def square(x):
    return x * x

# Apply function to each element using map
result = map(square, nums)

print(list(result))

one_to_4 =range(1,5)
times2 = lambda x: x*2
print(list(map(times2, one_to_4)))

#files - python object to write and write different file formats, file must be closed at end
#text modes
'''
Text modes 
r - Read, opens the file fior reading. File must exist.
w - Write, opens file for writing. Creates a new file if it doesn't exists or truncates(deletes) content if it does
a - append , opens file for writing. Adds data to the end of the file. Creates the file if it doesn't exist.
x - Exclusive creation, fails if already exist

Binary modes (Images, pdf etc)
rb - read binary
wb - write binary
ab - append binary
xb - Exclusive creation in binary mode
'''
with open("mydata.csv",mode='w', encoding="utf-8") as my_file:
    my_file.write("Hi, How is your day")

with open("mydata.csv",mode='r',encoding="utf-8") as my_file:
    print(my_file.read())
print(my_file.closed)








