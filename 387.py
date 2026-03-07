class Solution:
    def firstUniqChar(self, s: str) -> int:
        for letter in s:
            if s.count(letter) == 1:
                return s.find(letter)
        return -1

print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))
