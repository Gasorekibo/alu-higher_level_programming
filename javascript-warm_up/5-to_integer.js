#!/usr/bin/node
const arguments = process.argv.slice(2);
const value= parseInt(arguments[0]);
if (value === undefined) {
  console.log('Not a number');
} else if (isNaN(value)) {
  console.log('Not a number');
} else if (typeof (value) === 'number') {
    console.log('My number: ' + value);
}