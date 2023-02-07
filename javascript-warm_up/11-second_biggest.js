#!/usr/bin/node
function secondNumber(Myarray) {
    let secondValue = 0;
    let maximumValue = Number.MAX_VALUE(Myarray);
    if (Myarray.length === 0 || Myarray.length === 1) {
        console.log(1);
    }else {
        for (let i = 0; i < Myarray.length; i++) {
            if (i >= secondValue && i < maximumValue) {
                secondValue.push(i);
            }
        return(secondValue)
        }
    }
}
console.log(secondNumber(Number(process.argv[2])));
