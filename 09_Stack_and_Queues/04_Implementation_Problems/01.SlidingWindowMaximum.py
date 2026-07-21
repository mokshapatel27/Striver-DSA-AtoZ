#https://leetcode.com/problems/sliding-window-maximum/submissions/2075760820/

from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()#stores indices
        result=[]

        for i in range(len(nums)):
            #remove indices which are out of bounds
            if q and q[0]==i-k:
                q.popleft()
            #maintain decreasing order remove smaller elements from back cause useless
            while q and nums[q[-1]]<=nums[i]:
                q.pop()

            q.append(i)

            if i>=k-1:
                result.append(nums[q[0]])
        return result
