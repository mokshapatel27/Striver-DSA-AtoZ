#https://leetcode.com/problems/max-consecutive-ones-iii/description/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        maxlen=0

        for right in range(len(nums)):
            if nums[right]==0:
                k-=1
            # If flips go below 0, shrink the window from the left
            while k < 0:
            while k<0:
                if nums[left]==0:
                    k+=1
                left+=1

            maxlen=max(maxlen,right-left+1)

        return maxlen
