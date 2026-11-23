class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []

        nums.sort()

        res = []

        left_index = 0
        right_index = len(nums) - 1

        for fst_index in range(len(nums)):
            if nums[fst_index] == nums[fst_index - 1] and fst_index != 0:
                continue
            left_index = fst_index + 1
            right_index = len(nums) - 1

            while left_index < right_index:
                if nums[left_index] + nums[right_index] == -nums[fst_index]:
                    res.append([nums[fst_index], nums[left_index], nums[right_index]])
                    left_index += 1
                else:
                    if nums[left_index] + nums[right_index] > -nums[fst_index]:
                        right_index -= 1
                    else:
                        left_index += 1


        res = [list(x) for x in set(tuple(x) for x in res)]

        # print(res)

        return res


Solution().threeSum([-1, 0, 1, 2, -1, -4])  # Output: [[-1, -1, 2], [-1, 0, 1]]
Solution().threeSum([-5, 1, 4, 9])
# Solution().threeSum([0, 1, 1])  # Output: []
# Solution().threeSum([0, 0, 0])  # Output: [[0, 0, 0]]