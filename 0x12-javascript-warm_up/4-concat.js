#!/usr/bin/node
const ar = process.argv;
const _is = 'is';
if (ar[2] && ar[3]) {
  console.log(ar[2], _is, ar[3]);
} else if (ar[2] && !ar[3]) {
  console.log(ar[2], _is, 'undefined');
} else {
  console.log('undefined', _is, 'undefined');
}
