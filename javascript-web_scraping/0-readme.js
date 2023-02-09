#!/usr/bin/node
const fs = require('fs');
fs.readFile('Readme', 'utf-8', function (error, data) {
  console.error(error)
  return data
  }
);