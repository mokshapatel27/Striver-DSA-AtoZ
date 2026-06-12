#https://leetcode.com/problems/rearrange-array-elements-by-sign/submissions/2022565641/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        pos=0
        neg=1

        for num in nums:
            if num>0:
                res[pos]=num
                pos+=2
            else:
                res[neg]=num
                neg+=2
        return res
