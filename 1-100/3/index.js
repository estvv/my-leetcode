/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let n = s.length;
    let res = 0;

    for (let i = 0; i < n; i++) {
        let vis = new Array(26).fill(false);

        for (let j = i; j < n; j++) {
            if (vis[s.charCodeAt(j) - 'a'.charCodeAt(0)] === true)
                break;
            else {
                res = Math.max(res, j - i + 1);
                vis[s.charCodeAt(j) - 'a'.charCodeAt(0)] = true;
            }
        }
    }
    return res;
};
