#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];
  for (const key in list) {
    const element = list[key];
    reversedList.push(element);
  }
  return (reversedList);
};
