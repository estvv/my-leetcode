class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        self.res = []

        self.search(target, [], candidates)

        self.res = [list(t) for t in set(tuple(sorted(x)) for x in self.res)]

        # print(self.res)
        return self.res

    def search(self, remaining, current, available):
        if remaining == 0:
            self.res.append(current)
        elif remaining > 0:
            for number in available:
                self.search(remaining - number, current + [number], available)


Solution().combinationSum([2, 3, 6, 7], 7) # [[2, 2, 3], [7]]
Solution().combinationSum([2, 3, 5], 8) # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
Solution().combinationSum([2], 1) # []