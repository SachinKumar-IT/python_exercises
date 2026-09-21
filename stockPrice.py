def findmaxProfit(price):
    minPrice = float('inf')
    maxProfit =0

    for i in range(len(price)):
        if price[i] < minPrice:
            minPrice = price[i]
        elif price[i] - minPrice > maxProfit:
            maxProfit = price[i] - minPrice

    return maxProfit

price=[7,1,5,3,6,4]
maxProfit_value=findmaxProfit(price)
print("Maximum profit is:", maxProfit_value)