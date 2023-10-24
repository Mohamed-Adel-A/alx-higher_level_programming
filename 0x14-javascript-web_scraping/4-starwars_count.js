#!/usr/bin/node
// a script that prints the number of movies where the character “Wedge Antilles” is present.
// - The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
// - Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
// - You must use the module request

const request = require('request');
const APIurl = process.argv[2];

request(APIurl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const res = JSON.parse(body).results;
    console.log(res.reduce((count, film) => {
      return film.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
