#!/usr/bin/node
/*
  Write a script that prints x times “C is fun”
  Where x is the first argument of the script
  If the first argument can’t be converted to an integer, print
  “Missing number of occurrences”.
*/

/*
   process.argv is an array containing the command-line arguments passed
   when the Node.js process was launched. The first element will be node,
   the second element will be the name of the JavaScript file. The next
   elements will be any additional command-line arguments.
   Here, process.argv[2] is the first argument passed by the user.
*/
const arg1 = process.argv[2];
const num = Number.parseInt(arg1);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else if (num >= 1) {
  let i = 0;
  while (i < num) {
    console.log('C is fun');
    i++;
  }
}
