class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1
        middle = len(nums) // 2

        res = [-1, -1]

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                res[0] = middle
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        left = 0
        right = len(nums) - 1
        middle = len(nums) // 2

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                res[1] = middle
                left = middle + 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        # print(res)
        return res

Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
Solution().searchRange([5, 7, 7, 8, 8, 10], 6)
Solution().searchRange([], 0)

    # first try in O(n)
    # def searchRange(self, nums: list[int], target: int) -> list[int]:
    #     first_index = -1
    #     last_index = -1

    #     for i in range(len(nums)):
    #         if nums[i] == target:
    #             first_index = i
    #             break

    #     for i in range(len(nums) - 1, 0, -1):
    #         if nums[i] == target:
    #             last_index = i
    #             break

    #     return [first_index, last_index]
