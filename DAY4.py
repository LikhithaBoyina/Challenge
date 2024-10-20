def maxProfit(prices):
    # Initialize variables to store the minimum price and maximum profit
    min_price = float('inf')
    max_profit = 0
    
    # Iterate through the list of prices
    for price in prices:
        # Update the minimum price if the current price is lower
        if price < min_price:
            min_price = price
        # Calculate the profit if the stock is sold at the current price
        profit = price - min_price
        # Update the maximum profit if the current profit is higher
        if profit > max_profit:
            max_profit = profit
    
    return max_profit

# Example usage
prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]

print(maxProfit(prices1))  # Output: 5
print(maxProfit(prices2))  # Output: 0
