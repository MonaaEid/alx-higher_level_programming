#!/usr/bin/node
const ar = process.argv;
if (Math.floor(parseFloat(ar[2]))) {
    console.log('My number: ', ar[2]);
} else {
    console.log('Not a number');
}
// const intValue = Math.floor(parseFloat(ar[2]));
