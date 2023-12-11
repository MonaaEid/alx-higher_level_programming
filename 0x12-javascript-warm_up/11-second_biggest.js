#!/usr/bin/node
const ar = process.argv;
let maxNum; let prevNum = 0;
if (ar.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < ar.length; i++) {
    const element = Math.floor(parseFloat(ar[i]));
    if (!isNaN(element) && element > prevNum) {
      maxNum = element;
      prevNum = element;
    }
  }
  console.log(maxNum || 0);
}
