var groupAnagrams = function(strs) {
    let map = {};

    for (let str of strs) {
        const cleanStr = sortAlphabets(str);

        if (map[cleanStr] === undefined) {
            map[cleanStr] = [str];
        } else {
            map[cleanStr].push(str);
        }
    }
    return Object.values(map);
};

var sortAlphabets = function(text) {
    return text.split('').sort().join('');
};
