#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2]; // The first argument is the Movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    characterUrls.forEach((url, index) => {
      request(url, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
          return;
        }
        if (response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        } else {
          console.error('Failed to retrieve character, status code:', response.statusCode);
        }
      });
    });
  } else {
    console.error('Failed to retrieve movie, status code:', response.statusCode);
  }
});
