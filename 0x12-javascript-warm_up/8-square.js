#!/usr/bin/node
if (parseInt(process.argv[2])) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    for (let j = 0; j < parseInt(process.argv[2]); j++) { process.stdout.write('X'); }
    console.log(' ');
  }
} else {
  console.log('Missing size');
}
