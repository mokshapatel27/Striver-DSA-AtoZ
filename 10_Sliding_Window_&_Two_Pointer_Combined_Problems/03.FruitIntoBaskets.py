#https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket={}
        left=0
        maxlen=0

        for right in range(len(fruits)):
            fruit=fruits[right]
            basket[fruit]=basket.get(fruit,0)+1

            while len(basket)>2:
                leftfr=fruits[left]
                basket[leftfr]-=1
                if basket[leftfr]==0:
                    del basket[leftfr]
                left+=1

            maxlen=max(maxlen,right-left+1)
        return maxlen
