#!/usr/bin/node
const list = require('./100-data.js').list;
const computedArray = list.map((item, index) => item * index);
console.log(computedArray);
