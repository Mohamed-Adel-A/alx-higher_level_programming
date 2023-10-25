#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
// - The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// - Display one character name by line
// - You must use the Star wars API
// - You must use the module request

const request = require('request');
const APIurl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(APIurl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    const chara = content.characters;
    for (const i of chara) {
      request.get(i, function (error, response, bodyI) {
        if (error) {
          console.log(error);
        }
        const contentI = JSON.parse(bodyI);
        console.log(contentI.name);
      });
    }
  }
});
