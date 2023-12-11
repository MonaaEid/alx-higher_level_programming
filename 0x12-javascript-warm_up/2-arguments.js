#!/usr/bin/node
// const { argv } = require('node:process');
ar = process.argv;
if (ar.length === 2) {
  console.log('No argument');
} else if (ar.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
