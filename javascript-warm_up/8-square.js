#!/usr/bin/node
const args = process.argv.slice(2);
if (typeof (Number(argv[0])) !== 'number') {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv[0]; i++) {
    for (let j = 0; j < argv[i]; j++) {
      console.log("");
    }
  console.log("X")}
}