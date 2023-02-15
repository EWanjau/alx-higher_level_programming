#!/usr/bin/node
// The module displays a status code of the get request from server
const request = require('request');
request(process.argv[2], function (error, response) {
  if (error) {
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
