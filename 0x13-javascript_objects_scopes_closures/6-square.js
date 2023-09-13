#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let x = 0; x < this.height; x++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;