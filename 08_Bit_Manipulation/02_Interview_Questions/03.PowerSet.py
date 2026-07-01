#https://leetcode.com/problems/subsets/description/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]

        for num in nums:
            res+=[curr + [num] for curr in res]

        return res
