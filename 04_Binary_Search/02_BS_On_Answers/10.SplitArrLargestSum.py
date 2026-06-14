#https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low,high=max(nums),sum(nums)
        ans=high

        while low<=high:
            mid=(low+high)//2

            subarr=1
            currsum=0

            for num in nums:
                if currsum+num<=mid:
                    currsum+=num
                else:
                    subarr+=1
                    currsum=num

            if subarr<=k:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
