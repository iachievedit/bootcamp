#!/usr/bin/env node

// Unlike Python, Javascript needs a semicolon after each line of code
// And notice that Javascript comments start with // instead of #
bagsOfCoffee = 10;
ouncesPerBag = 12;

// Notice instead of print() we use console.log()
console.log("Bags of coffee:  ", bagsOfCoffee);
console.log("Ounces per bag:  ", ouncesPerBag);

// Like Python we can assign integers, floats, strings, etc.
aWholeNumber      = 7;
aFractionalNumber = 7.5;
aString           = 'How now brown cow';

// So far this looks very much like Python except the ;

console.log(aWholeNumber);
console.log(aFractionalNumber);
console.log(aString);

// Here's an array (also called a list) but we're going to use the
// var keyword to declare it

var aList = [1, 2, 3, 4];

// What's this var all about?  This is where there is a subtle difference
// in Javascript between variables and properties.  Try to ignore it for 
// now and focus on always using var to declare variables.

console.log(aList);

// Indexing in action
var theThirdElement = aList[2];
console.log("aList[2] = ", theThirdElement);

// And we come to Javascript dictionaries, but here they are
// referred to as hashes.  Same thing.

var aHash = {
	"key1":"value1",
	"key2":"value2"
};

console.log(aHash);

// Get one value from the hash
var aHashValue = aHash["key1"];
console.log(aHashValue);
