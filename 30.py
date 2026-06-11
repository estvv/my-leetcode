class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        res = []

        for word in words:
            if s.find(word) != -1:
                res.append(s.find(word))