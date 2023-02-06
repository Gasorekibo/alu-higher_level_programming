#!/usr/bin/node
function add(a, b) {
  if (typeof (a) || typeof (b) === undefined) {
    console.log('NaN');
  }else {
    return a + b;
    }
}
console.log(add());
