#!/usr/bin/node
const args = process.argv.slice(2);
if (typeof (Number(args[0])) !== 'number') {
  console.log('Missing number of occurrence');
} else {
  for (let i = 0; i < args[0]; i++) {
    console.log('C is fun');
  }
}
