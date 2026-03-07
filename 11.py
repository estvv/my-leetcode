class Solution:
    def maxArea(self, height: list[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        res = -1

        while left_index != right_index:
            res = max(res, min(height[left_index], height[right_index]) * abs(left_index - right_index))

            if height[left_index] < height[right_index]:
                left_index += 1
            else:
                right_index -= 1

        return res
