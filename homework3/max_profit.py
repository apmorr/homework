
def price_to_profit(prices):
    return [prices[i] - prices[i-1] if i > 0 else 0 for i in range(len(prices))]


def max_profit_crossing(L, left, right, median):
    max_left_sum = float('-inf')
    max_right_sum = float('-inf')

    left_sum = 0
    for i in range(median, left - 1, -1):
        left_sum += L[i]
        if left_sum > max_left_sum:
            max_left_sum = left_sum

    right_sum = 0
    for i in range(median + 1, right + 1):
        right_sum += L[i]
        if right_sum > max_right_sum:
            max_right_sum = right_sum

    return max_left_sum + max_right_sum

def max_profit(L, left, right):
    if left == right:
        return L[left]

    median = (left + right) // 2

    max_left = max_profit(L, left, median)
    max_right = max_profit(L, median + 1, right)
    max_crossing = max_profit_crossing(L, left, right, median)

    return max(max_left, max_right, max_crossing)

  
