#!/usr/bin/node
// The module read a fle and outputs the contents
const fs = require('fs');

const stringToWrite = process.argv[3];

fs.writeFile(process.argv[2], stringToWrite, (err) => {
  if (err) {
    console.error(err);
  }
});
