class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1

        while


    def getNumber(self, nums):
        return int(''.join(nums))

    def swap(self, nums, i, j):
        tmp = self.nums[j]
        self.nums[j] = self.nums[i]
        self.nums[i] = tmp
