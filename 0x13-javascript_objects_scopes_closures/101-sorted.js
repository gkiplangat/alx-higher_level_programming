#!/usr/bin/node

const { dict } = require('./101-data');

const ids = Object.values(dict);
const occurs = Object.keys(dict);

const newDict = {};
ids.forEach(id => {
  newDict[id] = [];
});

let index = 0;
ids.forEach(id => {
  newDict[id].push(occurs[index]);
  index++;
});

console.log(newDict);
