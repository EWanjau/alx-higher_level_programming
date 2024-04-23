#!/usr/bin/node
// The module read a fle and outputs the contents
const fs = require('fs');

fs.readFile(process.argv[2], (err, data) => {
  if (err) throw err;
  console.log(data.toString());
});
