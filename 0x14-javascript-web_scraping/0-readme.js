#!/usr/bin/node
// Write a script that reads and prints the content of a file.

// The first argument is the file path
// The content of the file must be read in utf-8
// If an error occurred during the reading, print the error object
// console err/err prints the error object

const fs = require('fs');
const filePath = process.argv[2]; // The first argument is the file path

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    // If an error occurred during the reading, print the error object
    console.error(err);
  } else {
    // If the file is read successfully, print its content
    console.log(data);
  }
});
