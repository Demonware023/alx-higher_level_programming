#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedByUser = {};

    todos.forEach(todo => {
      if (todo.completed) {
        if (!completedByUser[todo.userId]) {
          completedByUser[todo.userId] = 0;
        }
        completedByUser[todo.userId]++;
      }
    });

    for (const userId in completedByUser) {
      console.log(`{ '${userId}': ${completedByUser[userId]} }`);
    }
  } else {
    console.error('Error: Failed to get content from the URL, status code:', response.statusCode);
  }
});
