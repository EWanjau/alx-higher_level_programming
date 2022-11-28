#!/usr/bin/node
const array = process.argv.slice(2).map(element => Number.parseInt(element));
if (array.length < 2) {
  console.log(0);
} else {
  array.sort((a, b) => a - b);
  console.log(array[array.length - 2]);
}
