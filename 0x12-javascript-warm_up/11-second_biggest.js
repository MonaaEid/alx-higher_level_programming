#!/usr/bin/node
const ar = process.argv;

if (ar.length <= 3) {
  console.log(0);
} else {
    const args = process.argv.slice(2);
    const sortedArr = args.map(Number).sort((a, b) => b - a);
    console.log(sortedArr[1]);

    // return sortedArr[1] || 0;
//   for (let i = 2; i < ar.length; i++) {
//     const element = Math.floor(parseFloat(ar[i]));
//     if (!isNaN(element) && element > prevNum) {
//       maxNum = element;
//       prevNum = element;
//     }
//   }
}
