#!/usr/bin/node
const ar = process.argv;
let maxNum, prevNum = 0;
if (ar.length === 2 || ar.length === 3 ) {
    console.log(0);
} else {
    for (const key in ar) {
            const element = Math.floor(parseFloat(ar[key]));
            if (element > prevNum) {
                maxNum = element;
                prevNum =  element;
            }
        }
        console.log(maxNum);
    }
