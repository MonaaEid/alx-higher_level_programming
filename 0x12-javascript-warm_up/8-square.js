#!/usr/bin/node
const ar = process.argv;
const x = Math.floor(parseFloat(ar[2]));
if (!x) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let row = '';
    for (let j = 0; j < x; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
