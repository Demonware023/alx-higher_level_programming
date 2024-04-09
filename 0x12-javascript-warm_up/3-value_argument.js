#!/usr/bin/node
/* Write a script that prints the first argument passed to it:
   If no arguments are passed to the script, print “No argument”
   You must use console.log(...) to print all output.
*/

const arg = process.argv[2];

if (!arg) {
  console.log('No argument');
} else {
  console.log(arg);
}
