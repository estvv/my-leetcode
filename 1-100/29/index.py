class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = int(dividend / divisor)

        if res >= 2147483648:
            return 2147483647
        return res