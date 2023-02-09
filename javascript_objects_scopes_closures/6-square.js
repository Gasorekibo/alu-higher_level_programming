const Square = require('.5-square');
class Square extends Square {
    constructor (size) {
        super(size);
    }

    charPrint(c) {
        if (typeof(c) !== undefined) {
            console.log('c' * super(size));
        }
    }
}