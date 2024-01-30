#!/usr/bin/node

const request = require('request');
function helpRequest (arr, j) {
  if (j === arr.length) {
    return;
  }
  request(arr[i], function (err, response, body) {
    if (err) {
      console.error(err);
    }
    console.log(JSON.parse(body).name);
    helpRequest(arr, j + 1);
  });
}

request('http://swapi.co/api/films/' + process.argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  }
  const charac = JSON.parse(body).characters;
  helpRequest(charac, 0);
});