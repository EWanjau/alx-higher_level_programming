#!/usr/bin/node

const SuperSquare = require('./5-square');

class Square extends SuperSquare {
  charPrint (c) {
    if (!c) { c = 'X'; }
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}
module.exports = Square;
