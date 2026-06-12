#https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums):
        longestlen=0
        nset=set(nums)
        
        for i in nset:
            if i-1 not in nset:
                current=i
                currentst=1
                while current+1 in nset:
                    currentst+=1
                    current+=1
                longestlen=max(longestlen,currentst)
        return longestlen
