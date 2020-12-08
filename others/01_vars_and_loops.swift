#!/usr/bin/env swift

// Swift was developed by Apple to replace Objective-C
// You'll find it similar to Python and Javascript

var bagsOfCoffee = 10 // Swift uses // for comments but note no semicolon
var ouncesPerBag = 12

print ("Bags of coffee:  ", bagsOfCoffee)
print ("Ounces per bag:  ", ouncesPerBag)

// In the case of Swift, you can drop the semicolon but the 
// var is required.

// Swift also lets you declare the type of variable
// even though it can infer it

var aWholeNumber:Int = 7 // Note the variableName:variableType syntax

print ("aWholeNumber = ", aWholeNumber)

var aFractionalNumber:Float = 7.5
var aString:String = "How now brown cow." // Strings is Swift must use double quotes

// An array in Swift
var aList = [1, 2, 3 ,4]

// Unlike in Javascript and Python, Swift arrays can only have
// one type in them (all integers, all strings, etc.) unless you
// tell the compiler.

var cantDoThis:[Any] = [1, 2.3, "No"]

// And Swift supports dictionaries but it is best to provide the
// key type and the value type.
var aDictionary:[String:String] = [
	"key1": "value1",
	"key2": "value2"
]

//
// And loops
//

var someNumbers = [1, 4, 3, 12, 147]

for n in someNumbers {
	var nSquared = n*n
	print ("\(n) squared is \(nSquared)")
}

// Python had a range() function, Javascript didn't, but
// Swift does with a different syntax

print("Count from 0 up to 10")
for n in 0...10 {
	print(n)
}

// And "backwards" ranges the syntax is a little weirder
print("Count dowm from 10 to 0")
for n in (0...10).reversed() {
	print(n)
}

print("Count down again")
var x = 10
while x > 0 {
	print(x)
	x -= 1 // Swift doesn't have -- but does have the -= operator
}





