#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (c) {
    if (!c) { c = 'X'; }
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}
module.exports = Square;
