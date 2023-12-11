const { argv } = require('node:process');

// print process.argv
argv.forEach((val, index) => {
  if (argv.length() < 2) {
    console.log(`${index}: ${val}`);
  }
  // console.log(`${index}: ${val}`);
});
