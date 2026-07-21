#https://leetcode.com/problems/online-stock-span/description/

class StockSpanner:

    def __init__(self):
        self.stack=[]
        #keeps track in monotonic order
    def next(self, price: int) -> int:
        span=1#starts todays count at 1
        #is prev price <=todays price?
        while self.stack and self.stack[-1][0]<=price:
            prev_price,prev_span=self.stack.pop()
            span+=prev_span
        self.stack.append((price,span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
