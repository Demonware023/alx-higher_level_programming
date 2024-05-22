#!/usr/bin/node
// Write a script that prints the number of movies where the character “Wedge Antilles” is present.

// The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
// Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Error: failed to retrieve movies and characterID, Status Code:', response.statusCode);
  } else {
    const films = JSON.parse(body).results;
    const WedgeAntillesFilms = films.filter(film =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );
    console.log(WedgeAntillesFilms.length);
  }
});
