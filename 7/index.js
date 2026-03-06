/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let res = 0;
    let isNeg = x < 0;
    let num = Math.abs(x);

    while (num > 0) {
        let digit = num % 10;

        res = (res * 10) + digit;
        num = Math.trunc(num / 10);
    }

    if (isNeg) {
        res = -res;
    }

    const limit = 2 ** 31;

    if (res < -limit || res > limit - 1) {
        return 0;
    }

    return res;
};
