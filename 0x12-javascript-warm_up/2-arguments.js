#!/usr/bin/node
/*
   Write a script that prints a message depending of the number of argument
   passed; If no arguments are passed to the script, print “No argument" If
   only one argument is passed to the script, print “Argument found” 
   Otherwise, print “Arguments found”
*/

//process.argv is an array containing the command-line arguments passed.
argsCount = process.argv.length - 2;

if (argsCount === 0) {
  console.log('No argument');
} else if (argsCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
