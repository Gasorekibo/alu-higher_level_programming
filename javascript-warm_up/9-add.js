#!/usr/bin/node
function add(a, b) {
  if (typeof (a) === undefined || typeof (b) === undefined) {
    console.log('NaN');
  }else {
    return a + b;
    }
}
add(a, b);
