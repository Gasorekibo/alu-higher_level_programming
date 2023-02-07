#!/usr/bin/node
function factorial(args) {
  result = 1;
  if (typeof (args) === 'number') {
    for (let i = 1; i<= args; i++) {
        return (result *= i);
    }
} else if (Number(args) === NaN) {
        return(1);
} else {
        console.log('No answer');
    }
}

console.log(factorial(Number(process.argv[2])));