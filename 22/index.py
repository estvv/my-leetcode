class Solution:
    def generateParenthesis(self, n: int):
        res = []
        self.backtrack(res, n, "", 0, 0)
        return res

    def backtrack(self, res, n, current_string: str, open_count: int, closed_count: int):
        if len(current_string) == 2 * n:
            res.append(current_string)
            return

        if open_count < n:
            self.backtrack(res, n, current_string + "(", open_count + 1, closed_count)

        if closed_count < open_count:
            self.backtrack(res, n, current_string + ")", open_count, closed_count + 1)
