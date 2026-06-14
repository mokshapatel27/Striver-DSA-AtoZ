#https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right=max(weights),sum(weights)

        while left<right:
            mid=(left+right)//2

            currday,currwt=1,0
            for w in weights:

                if currwt+w>mid:
                    currday+=1
                    currwt=0
                currwt+=w

            if currday<=days:
                right=mid
            else:
                left=mid+1

        return left
