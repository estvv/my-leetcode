class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        res = ""
        cycle = 2 * numRows - 2

        for r in range(numRows):
            for i in range(r, len(s), cycle):
                res += s[i]
                diag_index = i + cycle - 2 * r
                if r > 0 and r < numRows - 1 and diag_index < len(s):
                    res += s[diag_index]
        return res
