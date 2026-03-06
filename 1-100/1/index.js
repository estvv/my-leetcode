/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let map = {};

    for (let i = 0; i < nums.length; i++) {
        let sub = map[target - nums[i]];

        if (sub != undefined) {
            return [i, sub];
        } else {
            map[nums[i]] = i;
        }
    }
    return [-1, -1];
};
