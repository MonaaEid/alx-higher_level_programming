#!/usr/bin/node
const fs = require('fs');
const request = require('request');

try {
  request.get(process.argv[2], (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      fs.writeFileSync(process.argv[3], body, 'utf8');
    }
  });
} catch (err) {
  console.error(err);
}
