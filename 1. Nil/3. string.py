# Strings , well loved and hated
# it's a default/primitive type in python

# Let's make a string

" This is a string "
' This is a string '
''' This is a string '''
""" This is a string """

# All above are strings only,they won't affect the code directly,so Let's try printing them

print("This is a string",'This is a string','''This is a string''',"""This is a string""")


# Strings in variables
s="Hello World"
print(s)

# String is a sequence, which means it is a collection of small elements which could be iterated
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
# This will print H e l l o 
# array starts from 0

# Let's take a part of the string, this is called slicing
part1=s[0:5]
print(part1)
# This will take "Hello", 5th element will be left, as it's String[StartNum:EndNum-1]

# If no number is given it takes the entire side of it
part2=s[0:]
print(part2)
# This will print the whole " Hello World"

# some more eg
part3=s[5:]
print(part3)
# This will print " World"

part4=s[2:4]
print(part4)
# This will print "llo"

# Numbers could be negative
Npart1=s[2:-3]
print(Npart1)
# negative number means, start from the right, this will print "llo wo"

# more eg
Npart2=s[-1:]
print(Npart2)
# This will print "d", ' This means start from the right and contine' but after 'd' there is nothing, so it just prints 'd'

Npart3=s[:-1]
print(Npart3)
# This will print "Hello worl", this means start from left and continue till the right extreme and stops at -1

# NOTE-: JUST HAVE FUN WITH THE STRINGS, TRY DIFFERENT THINGS AND YOU WILL FIND IT AS EASY AS TYPING ;)

#----------------------------------------------

# Sometimes we need to split the String into words
NewString="This is a good way of learning"
Words=NewString.split(" ")
print(Words)

# This will print a List of words present in the sentence, (more about list later)

#split(x), x is a delimiter , that is , the split funtion will separate on the basis of x

# split on the basis of ',' '.' '#' ' '
Eg="#This, could work. I# don't, Think# so"
print("\nThe Eg:",Eg)
print("For no argument",Eg.split()) # not giving an argument is same as split(" ")
print("For space",Eg.split(" "))
print("For period",Eg.split("."))
print("For comma",Eg.split(","))
print("For hash",Eg.split("#"))

