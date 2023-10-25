#!/usr/bin/node

const request = require('request');
const APIurl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

req.get(APIurl, function (error, response, body) {
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
