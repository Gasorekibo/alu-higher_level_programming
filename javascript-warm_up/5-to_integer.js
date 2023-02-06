#!/usr/bin/node
const args = process.argv.slice(2);
if (typeof (args[0] === 'number')) {
  console.log('My number: ' + args[0]);
} else if (typeof (args[0] === 'string')) {
  console.log('Not a number');
} else {
  console.log('Not a number');
}
