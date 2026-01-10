def maxProfit(prices):
        i = 0
        profit = 0
        smallest = prices[0]
        for j in range(1, len(prices)):
            if prices[j]<smallest:
                smallest=prices[j]
            else:
                profit = max (profit, prices[j] - smallest)
        return profit
