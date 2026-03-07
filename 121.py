class Solution:
    # def maxProfit(self, prices: list[int]) -> int:
    #     notes = {elem: 0 for elem in prices}

    #     print(notes)

    #     for i in range(len(prices)):
    #         for j in range(i + 1, len(prices)):
    #             notes[prices[i]] = max(notes[prices[i]], prices[j] - prices[i])

    #     return max(elem for elem in notes.values())

    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([1, 2, 3, 4, 5]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
