#!/usr/bin/env python3

# Variables are where we store things for the program to recall them
# Each variable has a name and a value

bagsOfCoffee = 10
ouncesPerBag = 12

print("Bags of coffee:  ", bagsOfCoffee)
print("Ounces per bag:  ", ouncesPerBag)

# I like to think of variables as "anything I need to keep track of"
# as my program runs

# Software developers have names for the types of values that are stored
# For example, I could store:
#
# - a whole number
# - a fractional number 
# - a sequence of characters

aWholeNumber      = 7   # integer or "int"
aFractionalNumber = 7.5 # floating point or "float"
aString           = 'How now brown cow.'

print(aWholeNumber)
print(aFractionalNumber)
print(aString)

# Python has a very powerful type called a list that's written like this
# Lists are also referred to as arrays - usually if someone is talking
# about an array they imply it will be "indexed"

aList = [1, 2, 3, 4]
print(aList)

# Here is indexing in action
theThirdElement = aList[2] # Indexes (the position in the list) start at 0


# There's another very powerful type called a dictionary.  Rather than
# indexing with an integer you index with a "key"
aDictionary = {
  "key1":  "value1",
  "key2":  "value2"
}

print(aDictionary)

# Print just one value
print(aDictionary['key2'])