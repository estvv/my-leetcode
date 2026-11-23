class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        letters = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        res = ''

        index = 0

        while index < len(values) or num != 0:
            if num >= values[index]:
                res += letters[index]
                num -= values[index]
            else:
                index += 1

        return res

Solution().intToRoman(3749)  # Output: "MMMDCCXLIX"
Solution().intToRoman(58)  # Output: "LVIII"
Solution().intToRoman(1994)  # Output: "MCMXCIV"