#!/usr/bin/node
const fs = require('fs');
const first = fs.readFileSync(process.argv[2], 'utf8'), second = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], first + second);
