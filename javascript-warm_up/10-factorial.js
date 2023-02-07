#!/usr/bin/node
result = 1;
function factorial(args) {
  if (typeof (args) === 'number') {
    for (let i = 1; i<= args; i++) {
        return (result *= i);
    }
} else if (isNaN(args)) {
        return(1);
} else {
        console.log('No answer');
    }
}

console.log(factorial(Number(process.argv[2])));
