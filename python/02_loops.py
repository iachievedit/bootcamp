#!/usr/bin/env python3

# Loops!
# Why do something once when you can do it multiple times?

someNumbers = [1, 4, 3, 12, 147]

for n in someNumbers:
	nSquared = n*n
	print("%d squared is %d" % (n, nSquared))

# Loop is a term used to describe a repeated sequence of instructions
# that are performed until a specific condition is met.  Sounds daunting, but
# the above code is an example of a loop in that we
#
# - squared numbers (repeated instructions)
# - until we ran out of numbers to square (a specific condition is met)
#
# Some might say the above is an example of iterating, but I see
# iteration and looping as one in the same.

# Another typical loop, counting from one number to another:

print("Count from 0 up to 10")
for i in range(0, 10):
  print(i)

# Or we can count down
print("Count from 10 down to 0")
for i in range(10, 0, -1):
  print(i)

# We've seen two examples of loops that are iterators (processing items in a list)
# Now let's look at one that is based a logic condition
print("Count from 10 down to 1 with a while loop")
x = 10
while x > 0:
  print(x)
  x = x - 1

# These are very simple examples of loops but in general loops
# are designed to "do something multiple times until a condition is met"

