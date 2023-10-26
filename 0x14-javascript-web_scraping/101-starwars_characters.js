#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
// - The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// - Display one character name by line
// - You must use the Star wars API
// - You must use the module request

const request = require('request');
const APIurl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

function getcharactersNames (charactersData, i) {
  request(charactersData[i], function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      if (i + 1  < charactersData.length) {
        getcharactersNames(charactersData, i + 1)
      }
    }
  });
}

request.get(APIurl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const charactersData = JSON.parse(body).characters;
    getcharactersNames(charactersData, 0)
  }
});
