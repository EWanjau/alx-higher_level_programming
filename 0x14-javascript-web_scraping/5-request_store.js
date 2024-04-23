#!/usr/bin/node
// The module displays reads from a webpage and writes the info on a file
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
