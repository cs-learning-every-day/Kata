from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [(amount + 1)] * (amount + 1)
        dp[0] = 0
        for i in range(0, amount + 1):
            for coin in coins:
                if i < coin:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]
