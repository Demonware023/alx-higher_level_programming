#!/usr/bin/node
// Write a script that writes a string to a file.

// The first argument is the file path
// The second argument is the string to write
// The content of the file must be written in utf-8
// If an error occurred during while writing, print the error object
const fs = require('fs');
const filePath = process.argv[2]; // The first argument is the file path
const StringToWrite = process.argv[3]; // The second argument is the string to write

fs.writeFile(filePath, StringToWrite, 'utf8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`The string "${StringToWrite}" was successfully written to ${filePath}`);
  }
});
