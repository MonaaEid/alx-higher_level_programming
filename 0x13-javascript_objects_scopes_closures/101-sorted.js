#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const key in dict) {
  const element = dict[key];
  if (newDict[element] === undefined) {
    newDict[element] = [key];
  } else {
    newDict[element].push(key);
  }
  // console.log(key + ':' + element)
}

console.log(newDict);
