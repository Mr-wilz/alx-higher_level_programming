#!/usr/bin/env node
const fs = require('fs');
// Check if the file path is provided as an argument
if (process.argv.length < 3) {
  console.error('File path is missing.');
  process.exit(1);
}
const filePath = process.argv[2];
// Read the content of the file
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  // Print the content of the file
  console.log(data);
});
