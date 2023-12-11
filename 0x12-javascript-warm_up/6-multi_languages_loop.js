#!/usr/bin/node
const arr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
for (const item in arr) {
  if (arr.hasOwnProperty.call(arr, item)) {
    const element = arr[item];
    console.log(element);
  }
} {

}
