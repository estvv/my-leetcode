# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         best = ""
#         for i in range(len(s)):
#             tmp = ""
#             for j in range(i, len(s)):
#                 tmp += s[j]
#                 if tmp == ''.join(reversed(tmp)) and len(tmp) >= len(best):
#                     best = tmp
#         return best

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        best = ""
        for i in range(len(s)):
            pal1 = self.expand_around_center(s, i, i)
            pal2 = self.expand_around_center(s, i, i + 1)

            if len(pal1) > len(best):
                best = pal1
            if len(pal2) > len(best):
                best = pal2
        return best


    def expand_around_center(self, s, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]
