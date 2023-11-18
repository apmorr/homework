
def price_to_profit(prices):
    return [prices[i] - prices[i-1] if i > 0 else 0 for i in range(len(prices))]
  
