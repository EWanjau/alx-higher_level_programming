#!/usr/bin/node
// The module displays reads from a webpage and writes the info on a file
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const dic = {};
    const data = JSON.parse(body);
    for (const task of data) {
      if (task.completed) {
        if (dic[task.userId]) {
          dic[task.userId] = 1;
        }
      }
    }
    console.log(dic);
  }
});
