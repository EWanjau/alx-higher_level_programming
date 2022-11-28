#!/usr/bin/node
if (process.argv.length == 2) {
  console.log('No argument');
} else {
  console.log(process.argv.slice(2));
}
