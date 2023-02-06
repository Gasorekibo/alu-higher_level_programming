#!/usr/bin/node
const args = process.argv.slice(2);
if (typeof (Number(args[0])) !== 'number') {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[0]; i++) {
    for (let j = 0; j < args[i]; j++) {
      console.log("");
    }
  console.log("X".repeat(i));
}
}
