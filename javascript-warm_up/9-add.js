#!/usr/bin/node
function add (a, b) {
  if ((typeof (a) === 'undefined') || (typeof (b) === 'undefined')) {
    console.log('NaN');
  } else if ((typeof (a) === 'number') && (typeof (b) === 'number')) {
    console.log(a + b);
  } else {
    console.log('NaN');
  }
}
add(Number(process.argv[2]), Number(process.argv[3]));
