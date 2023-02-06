#!/usr/bin/node
const args = process.argv.slice(2);
if (typeof (Number(args[0])) !== 'number') {
  console.log('Missing size');
} else if (args[0] === 'Nop') {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[0]; i++) {
    console.log('X'.repeat(args[0]));
  }
}
