#!/usr/bin/node
const fs = require('fs');
fs.readFile('Readme', 'utf-8', function (err, data) {
  if (err) {console.log(err)}
  console.log(data);
  }
);