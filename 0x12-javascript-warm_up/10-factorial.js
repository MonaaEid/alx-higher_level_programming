#!/usr/bin/node
function factorialNum (n) {
  if (n === 0 || n === 1) {
    return 1;
  }
  const result = n * factorialNum(n - 1);
  return (result);
}
const ar = process.argv;
const x = Math.floor(parseFloat(ar[2]));
if (!x) {
  console.log(1);
} else {
  console.log(factorialNum(x));
}
