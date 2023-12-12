#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
//   return num => num.toString(base);
  // convertedNumber = toString(base);
  // return (convertedNumber);
};
// let myConverter = converter(10);

// console.log(myConverter);
// myConverter(555);
// converter(454)(16);
// console.log(myConverter(12));
// console.log(myConverter(89));

// myConverter = converter(16);
