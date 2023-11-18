
def price_to_profit(prices):
    return [prices[i] - prices[i-1] if i > 0 else 0 for i in range(len(prices))]


def max_profit_crossing(L, left, right, median):
    least_buyL = L[median]
    high_sellR = L[median + 1]

    for i in range(median - 1, -1, -1):
        least_buyL = min(Least_buyL, L[i])
    
    for i in range(median + 2, right + 1):
        high_sellR = max(high_sellR, L[i])

    return high_sellR - least_buyL

def max_profit(L, left, right):
    if left == right:
        return L[left]

    median = (left + right) // 2

    max_left = max_profit(L, left, median)
    max_right = max_profit(L, median + 1, right)
    max_crossing = max_profit_crossing(L, left, right, median)

    return max(max_left, max_right, max_crossing)

  
