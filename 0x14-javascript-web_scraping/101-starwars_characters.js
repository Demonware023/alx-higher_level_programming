#!/usr/bin/node
const request = require('request');

function fetchCharacterName(characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) return reject(error);
      if (response.statusCode !== 200) {
        return reject(new Error('Failed to load character'));
      }
      const character = JSON.parse(body);
      resolve(character.name);
    });
  });
}

const movieID = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request(apiUrl, async (error, response, body) => {
  if (error) {
    return console.error('Error:', error);
  }
  if (response.statusCode !== 200) {
    return console.error('Failed to retrieve movie, status code:', response.statusCode);
  }

  const movie = JSON.parse(body);
  const characterPromises = movie.characters.map(fetchCharacterName);

  try {
    const characterNames = await Promise.all(characterPromises);
    characterNames.forEach(name => {
      console.log(name);
    });
  } catch (err) {
    console.error('Failed to retrieve character names:', err);
  }
});
