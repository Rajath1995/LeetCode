class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = 0
        max_val = 0
        max_diff = 0
        for index, number in enumerate(prices):
            for ind, num in enumerate(prices):
                if ind > index and (num - number) > max_diff:
                    max_diff = num - number
                    min_val = number
                    max_val = num
        return max_diff
