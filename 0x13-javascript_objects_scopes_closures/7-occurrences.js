#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const key in list) {
    const element = list[key];
    if (element === searchElement) {
      count++;
    }
  }
  return (count);
};
