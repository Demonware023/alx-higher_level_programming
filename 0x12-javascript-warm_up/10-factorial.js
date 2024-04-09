#!/usr/bin/node
/*
   Write a script that computes and prints a factorial:
   The first argument is integer (argument can be cast as integer)
   used for computing the factorial.
   Factorial of NaN is 1.
   You must do it recursively.
   You must use a function.
*/

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return (1);
  } else {
    return n * factorial(n - 1);
  }
}

const num = Number.parseInt(process.argv[2]);
console.log(factorial(num));
