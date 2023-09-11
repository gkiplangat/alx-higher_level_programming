#!/usr/bin/node
const { argv } = require('process');

// Check if there are fewer than 3 arguments (script name + 1 argument)
if (argv.length <= 3) {
  console.log('0'); 
} else {
  let numsSorted = [];
  for (let n = 2; n < argv.length; n++) {
    const curr = parseInt(argv[n]);
    numsSorted = insertSorted(curr, numsSorted);
  }
  console.log(numsSorted[(numsSorted.length) - 2]);
}


function insertSorted (num, arr) {
  if (!arr) {
    return [num];
  }

  for (let n = 0; n < arr.length; n++) {
    if (arr[n] >= num) {
      return [...arr.slice(0, n), num, ...arr.slice(n)];
    }
  }

  return [...arr, num];

