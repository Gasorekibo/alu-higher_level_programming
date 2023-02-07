#!/usr/bin/node
function factorial (a) {
    result = 1;
    if (isNaN(a)){
        return 1;
    } else {
        for (let i= 1; i<=a; i++) {
            return(result * i);
        }
    }
}
console.log(factorial(Number(process.argv[2])));
