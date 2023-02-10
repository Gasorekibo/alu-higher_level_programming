#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[3];
fs.writeFile(filePath, 'utf-8', (error, content) => {
    if (error) {
        console.log(error); }
    console.log(content);
})
