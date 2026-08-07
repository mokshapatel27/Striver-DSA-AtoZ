# https://leetcode.com/problems/binary-subarrays-with-sum/description/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        '''exact(goal)=atmost(goal)-atmost(goal-1)'''
        def numSubarraysAtMost(k: int) -> int:
            if k < 0:
                return 0

            left=0
            currsum=0
            count=0

            for right in range(len(nums)):
                currsum+=nums[right]

                while currsum>k:
                    currsum-=nums[left]
                    left+=1
                count+=right-left+1
            return count
        return numSubarraysAtMost(goal) - numSubarraysAtMost(goal - 1)

