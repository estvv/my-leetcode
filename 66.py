class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return [int(x) for x in str(int(''.join(str(x) for x in digits)) + 1)]
