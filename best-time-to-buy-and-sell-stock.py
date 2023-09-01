def maxProfit(prices):
    left, maxProfit = prices[0], 0
    for i in range(0, len(prices)-1):
        if left > prices[i+1]:
            left = prices[i+1]
        elif left < prices[i+1] and prices[i+1] - left > maxProfit:
            maxProfit = prices[i+1] - left
    return maxProfit
print(maxProfit([7,1,5,3,6,4]))