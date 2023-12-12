#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];
  const i = list.length;
  for (let k = i - 1; k >= 0; k--) {
    const element = list[k];
    reversedList.push(element);
  }
  return (reversedList);
};
