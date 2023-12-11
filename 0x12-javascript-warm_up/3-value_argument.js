#!/usr/bin/node
const ar = process.argv;
if (ar[2]) {
  console.log(ar[2]);
} else {
  console.log('No argument');
}
