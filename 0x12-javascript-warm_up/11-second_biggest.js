#!/usr/bin/node
const ar = process.argv;
let maxNum; let prevNum = 0;
if (ar.length === 2) {
  console.log(0);
} else if (ar.length === 3) {
  console.log(0);
} else {
  for (const key in ar) {
    const element = Math.floor(parseFloat(ar[key]));
    if (!isNaN(element) && element > prevNum) {
      maxNum = element;
      prevNum = element;
    }
  }
  console.log(maxNum);
}
