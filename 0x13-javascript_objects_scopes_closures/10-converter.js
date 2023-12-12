#!/usr/bin/node
exports.converter = function (base) {
    // return function (num) {
    //     return num.toString(base);
    // }
    return num => num.toString(base);
    // convertedNumber = toString(base);
    // return (convertedNumber);
}