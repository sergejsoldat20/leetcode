class Solution(object):
    def maxProfit(self, prices):

        max_profit = 0
        left, right = 0, 1

        while right < len(prices):

            # ako je lijevi pointer manji od desnog onda provjerimo koliki je profit
            if prices[left] < prices[right]:
                curr_profit = prices[right] - prices[left]
                max_profit = max(curr_profit, max_profit)

            else:
                left = right
            right += 1

        return max_profit


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
