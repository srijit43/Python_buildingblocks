def max_profit(prices):
    l, r = 0, 1  # Initialize two pointers
    max_profit = 0  # Variable to store maximum profit

    while r < len(prices):
        if prices[r] < prices[l]:  # If we find a lower price, move `l`
            l = r  
        else:
            max_profit = max(max_profit, prices[r] - prices[l])  # Update max profit
        r += 1  # Move right pointer forward

    return max_profit

# Example usage:
prices = [12, 10, 7, 9, 16, 18, 14]
print(max_profit(prices))  # Output: 11 (Buy at 7, Sell at 18)


    


        
        