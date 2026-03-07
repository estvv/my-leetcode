/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    s = s.trim();

    if (s.length == 0) {
        return 0;
    }

    let isNeg = false;

    let i = 0;

    if (s[0] == '-') {
        isNeg = true;
        s = s.slice(1, s.length);
    } else if (s[0] == '+') {
        s = s.slice(1, s.length);
    }

    if (s[i] < '0' || s[i] > '9') {
        return 0;
    }

    i = 0;

    while (i < s.length && (s[i] >= '0' && s[i] <= '9')) {
        i++;
    }

    s = s.slice(0, i);

    let res = Number(s);

    if (isNeg) {
        res = -res;
    }

    if (res <= Math.pow(-2, 31)) {
        return Math.pow(-2, 31);
    }
    if (res >= Math.pow(2, 31) - 1) {
        return Math.pow(2, 31) - 1;
    }
    return res;
};
