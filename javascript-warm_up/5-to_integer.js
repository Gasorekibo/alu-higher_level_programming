#!/usr/bin/node
const args = process.argv.slice(2);
const value = parseInt(args[0]);
if (value === undefined) {
  console.log('Not a number');
} else if (isNaN(value)) {
  console.log('Not a number');
} else if (typeof (value) === 'number') {
  console.log('My number: ' + value);
}
