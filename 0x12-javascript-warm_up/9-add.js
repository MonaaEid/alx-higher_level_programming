#!/usr/bin/node
const ar = process.argv;
const a = Math.floor(parseFloat(ar[2]));
const b = Math.floor(parseFloat(ar[3]));
if (!a || !b) {
  console.log(NaN);
} else {
  console.log(a + b);
}
