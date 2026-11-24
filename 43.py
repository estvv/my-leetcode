class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]

        digits = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            retenue = 0

            for j in range(len(num2)):
                value = (ord(num1[i]) - 48) * (ord(num2[j]) - 48) + digits[i + j] + retenue
                digits[i + j] = value % 10
                retenue = value // 10

            digits[i + len(num2)] = retenue

        while len(digits) > 1 and digits[-1] == 0:
            digits.pop()

        res = ""
        for digit in digits[::-1]:
            res += chr(digit + 48)

        return res

# Solution().multiply("2", "3")
Solution().multiply("123", "456")
