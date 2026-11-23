class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pivot_index = len(nums) - 1

        while pivot_index > 0:
            if nums[pivot_index] > nums[pivot_index - 1]:
                break
            else:
                pivot_index -= 1

        if pivot_index == 0:
            nums.sort()
            print(nums)
            return

        pivot_index -= 1

        # print(nums)
        # print(nums[pivot_index])

        swap_index = 0

        for i in range(len(nums) - 1, 0, -1):
            # print(nums[i], nums[pivot_index])
            if nums[i] > nums[pivot_index]:
                swap_index = i
                break

        nums[pivot_index], nums[swap_index] = nums[swap_index], nums[pivot_index]
        nums[pivot_index + 1:] = sorted(nums[pivot_index + 1:])

        # print(nums)

Solution().nextPermutation([1, 2, 3]) # [1, 3, 2]
Solution().nextPermutation([3, 2, 1]) # [1, 2, 3]
Solution().nextPermutation([1, 1, 5]) # [1, 5, 1]
Solution().nextPermutation([1, 3, 2]) # [2, 1, 3]
