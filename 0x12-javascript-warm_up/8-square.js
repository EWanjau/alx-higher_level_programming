#!/usr/bin/node
const num = Number.parseInt(process.argv[2]);
if (!num) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
