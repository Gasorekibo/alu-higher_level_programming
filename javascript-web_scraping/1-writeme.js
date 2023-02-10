#!/usr/bin/node
const fs = require('fs');
const Path = process.argv[3];
fs.writeFile(Path, 'hello', (error, content) => {
  if (error) {
    console.log(error); }
  console.log(content.toString());
})
