#!/usr/bin/node
// addition of two integers
function add (a, b) {
  a = parseInt(process.argv[2]);
  b = parseInt(process.argv[3]);
  const add = a + b;
  return add;
}
console.log(add());
