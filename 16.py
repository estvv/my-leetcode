class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        nums.sort()

        res = float('+inf')
        dist = float('+inf')

        left_index = 0
        right_index = len(nums) - 1

        for fst_index in range(len(nums)):
            left_index = fst_index + 1
            right_index = len(nums) - 1

            while left_index < right_index:
                if abs(nums[left_index] + nums[right_index] + nums[fst_index] - target) < dist:
                    dist = abs(nums[left_index] + nums[right_index] + nums[fst_index] - target)
                    res = nums[left_index] + nums[right_index] + nums[fst_index]
                else:
                    if nums[left_index] + nums[right_index] + nums[fst_index] > target:
                        right_index -= 1
                    else:
                        left_index += 1

        # print(res)

        return res

Solution().threeSumClosest([-1, 2, 1, -4], 1) # Should be 2
Solution().threeSumClosest([0, 0, 0], 1) # Should be 0
Solution().threeSumClosest([10,20,30,40,50,60,70,80,90], 1)
