#!/usr/bin/node
if (process.argv[2] == null) {
  console.log(0);
} else if (process.argv.length == 3) {
  console.group(0);
} else {
  let max_num = process.argv[2];
  for (let i = 0; i < process.argv.length; i++) {
    if (process.argv[i] > max_num) { max_num = process.argv[i]; }
    diff = max_num - process.argv[i];
  }
}
