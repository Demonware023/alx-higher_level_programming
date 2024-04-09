#!/usr/bin/node
/*
   Write a script that prints the addition of 2 integers:
   The first argument is the first integer
   The second argument is the second integer
   You have to define a function with this prototype: function add(a, b)
*/

// Add Function
function add (a, b) {
  return (a + b);
}

const num1 = Number.parseInt(process.argv[2]);
const num2 = Number.parseInt(process.argv[3]);

const len = process.argv.length;

if (len <= 2) {
  console.log('NaN');
} else {
  console.log(add(num1, num2));
}
