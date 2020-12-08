#!/usr/bin/env node

// Loops in Javascript are similar to loops in Python
// but the syntax is different.

var someNumbers = [1, 4, 3, 12, 147];

console.log("Iterating (looping) through a list");
for (var n in someNumbers) {
	var nSquared = n*n;
	console.log(`${n} squared is ${nSquared}`);
}

// Unlike Python, Javascript for loops are typed as
// for (expression) { statement1; statement2; ... statementN; }

// Javascript also does not have a built-in range() function like
// Python did, but that's okay we can use this.  This is a
// classic for loop that one would encounter in C (except for the
// var keyword)
console.log("Counting up!");
for (var i = 0; i <= 10; i++) {
	console.log(i);
}

// The expression is broken into 3 parts
// - the starting condition (i = 0)
// - the looping condition (as long as the loop condition is true)
// - the increment statement
// On the first iteration i is set to 0
// If the loop condition is true (0 is less than or equal to 10),
// execute what is in the block
// Increment i by 1 (++ is shorthand for "add one")

// As you can see, incrementing is in the eye of the beholder,
// as it can be a decrement if you want it to be...
console.log("Counting down with a for loop");
for (var i = 10; i >= 0; i--) {
	console.log(i);
}

// Like Python, Javascript also has a while loop
console.log("Counting down with a while loop");
var x = 10;
while (x > 0) {
	console.log(x);
	x--;
}

// At this point you can see that Javascript and Python are
// similar in their ability to store variables and have looping
// constructs.  This is not by accident, as all languages
// share this basic idea.

