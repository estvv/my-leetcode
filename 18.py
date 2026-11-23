class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        if len(nums) < 4:
            return []

        nums.sort()

        res = []

        left_index = 0
        right_index = len(nums) - 1

        for a_index in range(len(nums)):
            for b_index in range(a_index + 1, len(nums)):
                left_index = b_index + 1
                right_index = len(nums) - 1

                while left_index < right_index:

                    if nums[left_index] + nums[right_index] + nums[a_index] + nums[b_index] == target:
                        res.append(sorted([nums[left_index], nums[right_index], nums[a_index], nums[b_index]]))
                        left_index += 1
                    else:
                        if nums[left_index] + nums[right_index] + nums[a_index] + nums[b_index] > target:
                            right_index -= 1
                        else:
                            left_index += 1


        res = [list(x) for x in set(tuple(x) for x in res)]

        return res


Solution().fourSum([1, 0, -1, 0, -2, 2], 0)  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
Solution().fourSum([2, 2, 2, 2, 2], 8)  # Output: [[2, 2, 2, 2]]
