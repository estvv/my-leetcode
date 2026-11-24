class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        self.res = []

        self.search(target, [], sorted(candidates))

        # print(self.res)
        return self.res

    def search(self, remaining, current, available: list[int]):
        if remaining == 0:
            self.res.append(current)
        elif remaining > 0:
            for i in range(len(available)):
                if i != 0 and available[i] == available[i - 1]:
                    continue
                self.search(remaining - available[i], current + [available[i]], available[i + 1:])


Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) # [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]
Solution().combinationSum2([2, 5, 2, 1, 2], 5) # [[1, 2, 2], [5]]
