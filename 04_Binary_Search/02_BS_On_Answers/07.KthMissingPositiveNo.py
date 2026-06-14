#https://leetcode.com/problems/kth-missing-positive-number/submissions/2031837808/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left,right=0,len(arr)-1

        while left<=right:
            mid=(left+right)//2
            missing=arr[mid]-(mid+1)

            if missing<k:
                left=mid+1
            else:
                right=mid-1
        return left+k
