#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    let n = 0;
    for (let j = 0; j < list.length; j++) {
      if (list[j] === searchElement) {
        n++;
      }
    }
    return n;
  };