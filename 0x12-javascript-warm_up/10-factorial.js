#!/usr/bin/node
// function calculates factorial
function factorial (a) {
  a = parseInt(process.argv[2]);
  if (!a) {
    return 1;
  }
  return (a * factorial(a - 1));
}

console.log(factorial());
