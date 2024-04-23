#!/usr/bin/node
// The module displays a corresponding name of episode of a star wars episode
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
} else if (JSON.parse(body).results) {
    let counter = 0;
    for (const movies of JSON.parse(body).results) {
        for (const character of movies.characters) {
            if (characters.slice(-3, -1) === '18') {
                counter++;
            }
        }
    }
    console.log(counter);
}
});
