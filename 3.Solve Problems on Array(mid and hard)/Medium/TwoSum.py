#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}

        for i, A in enumerate(nums):
            B=target-A

            if B in seen:
                return [seen[B],i]

            else: 
                seen[A]=i
