#!/usr/bin/node
function factorial_num (n) {
  if (n === 0 || n === 1) {
    return 1;
  }
  const result = n * factorial_num(n - 1);
  return (result);
}
const ar = process.argv;
const x = Math.floor(parseFloat(ar[2]));
if (!x) {
  console.log(1);
} else {
  console.log(factorial_num(x));
}
