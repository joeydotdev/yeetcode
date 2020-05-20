class StockSpanner:

    def __init__(self):
        self.s = []
        

    def next(self, price: int) -> int:
        amt = 1
        while len(self.s) > 0 and self.s[-1][0] <= price:
            top_price, top_amt = self.s.pop()
            amt += top_amt
        self.s.append((price, amt))
        return amt

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


"""


amt=60

1

2

[100, 80, 60, 70, 60, 75, 85]
[1,   1,   1,  2,  1,  4,  6]

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.


we want to find # of days in which:
threshold = prices[i]

from i, i-1, ..., 0


N log N approach:
- build a sorted array as you walk through input


[100]
"""