#!/usr/bin/node
const fs = require('fs');
const Path = process.argv[3];
fs.writeFile(Path, 'utf-8', 'hello', (error, content) => {
  if (error) {
    console.log(error); }
  console.log(content);
})
