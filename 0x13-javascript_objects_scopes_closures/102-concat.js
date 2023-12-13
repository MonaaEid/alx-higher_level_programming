#!/usr/bin/node
const fs = require('fs');
const ar = process.argv;
const fileOne = ar[2];
const fileTwo = ar[3];
const fileDest = ar[4];

const firstContent = fs.readFileSync(fileOne, 'utf8');
const secondContent = fs.readFileSync(fileTwo, 'utf8');
const conContent = firstContent + secondContent;
fs.writeFileSync(fileDest, conContent);
// console.log(fileOne);
