/**
 * @param {string} s
 * @return {boolean}
 */

var isValid = function(s) {
    let charMap = {'(': ')', '[': ']', '{': '}'}
    let stack = []

    for (let char of s) {
        if (char == '(' || char == '[' || char == '{') {
            stack.push(char)
        } else {
            tmp = stack.pop();

            if (char != charMap[tmp]) {
                return false
            }
        }
    }
    if (stack.length > 0) {
        return false
    }
    return true
};
