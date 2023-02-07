#!/usr/bin/node
function factorial(args) {
  result = 1;
  if (typeof (args) === 'number') {
    for (let i = 1; i<= args; i++) {
        result = 1 * i;
    }
} else if (Number(args) === NaN) {
        result = 1;
} else {
        console.log('No answer');
    }
  console.log(result);
}

factorial(Number(args));