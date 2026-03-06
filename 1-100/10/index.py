class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        j = 0

        while i < len(s) and j < len(p):
            if i > j:
                return False
            if p[j] == '.':
                
            if p[j] != s[i] and p[j] != '.':
                return False
            i += 1
            j += 1
        return i == len(s) and j == len(p)

print(Solution().isMatch("aa", "a"))
print(Solution().isMatch("aa", "a*"))
print(Solution().isMatch("ab", ".*"))
print(Solution().isMatch("aab", "c*a*b"))
print(Solution().isMatch("mississippi", "mis*is*p*."))