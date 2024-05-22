#!/usr/bin/node
// Write a script that gets the contents of a webpage and stores it in a file.

// The first argument is the URL to request
// The second argument the file path to store the body response
// The file must be UTF-8 encoded
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3]; // The second argument is the file path to store the body response

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Error: Failed to get content from the URL, status code:', response.statusCode);
  } else {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error('Error writing to file:', err);
      } else {
        console.log(`Content saved to ${filePath}`);
      }
    });
  }
});
