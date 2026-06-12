#https://leetcode.com/problems/maximum-subarray/submissions/2022071679/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current=nums[0]
        max_sum=nums[0]

        for num in nums[1:]:
            current=max(num,current+num)
            max_sum=max(max_sum,current)

        return max_sum
