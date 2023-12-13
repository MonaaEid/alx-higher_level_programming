#!/usr/bin/node
const fs = require('fs');
const ar = process.argv;
const fileOne = ar[2];
const fileTwo = ar[3];
const fileDest = ar[4];

firstContent = fs.readFileSync(fileOne, 'utf8');
secondContent = fs.readFileSync(fileTwo, 'utf8');
conContent = firstContent + secondContent;
fs.writeFileSync(fileDest, conContent);
// console.log(fileOne);
