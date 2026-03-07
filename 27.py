class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0

        while i < len(nums):
            if nums[i] == val:
                nums.remove(val)
            else:
                i += 1
        return i
