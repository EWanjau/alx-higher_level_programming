#!/usr/bin/node
// function that prints arguments passed to it
if (process.argv.length === 2) {
  console.log('No argument');
} else {
  console.log(process.argv.slice(2));
}
