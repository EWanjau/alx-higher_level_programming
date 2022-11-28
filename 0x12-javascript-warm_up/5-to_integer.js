#!/usr/bin/node
// a function that uses try and catch to print
if (Number(process.argv[2])) {
  console.log('My number: ' + Number(process.argv[2]));
} else {
  console.log('Not a number');
}
