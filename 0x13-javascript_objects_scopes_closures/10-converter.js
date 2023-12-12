#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
//   return num => num.toString(base);
  // convertedNumber = toString(base);
  // return (convertedNumber);
};
