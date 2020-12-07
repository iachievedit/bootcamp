#!/usr/bin/env python3

# Computers are great at executing instructions based upon
# a condition.  We saw that with loops, now we're going to look
# at running code based upon

# This is subjective, but most would agree that 0-32 degrees
# is frigid, 33-45 is cold, 46-64 is cool, and 65-75 is warm,
# and we'll just say 76 and over is hot.  Maybe > 100 is very hot.

theTemperature = 47

if theTemperature <= 32:
	print("It's frigid")

if theTemperature > 32 and theTemperature < 46:
	print("It's cold")

if theTemperature >= 46 and theTemperature < 65:
	print("It's cool")

# Try writing the statements for the rest of the ranges
# Notice that in general, we are writing "if" followed by
# some logic.  If <this is true>: do this.  There's an 
# implicit, "otherwise, move on and don't do this".

# In code you can see that some people will write
# If this is not true, then do this.  For example:

theTemperature = 211
boiling        = True if theTemperature >= 212 else False

if not boiling:
	print("%d is not boiling, just %d degrees to go" % (theTemperature, 212 - theTemperature))

# For what it's worth, the above code is klunky but is valid (other than the grammar error)