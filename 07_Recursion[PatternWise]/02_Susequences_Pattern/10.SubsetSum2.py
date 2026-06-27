#https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int],path:List[int]=None) -> List[List[int]]:
        #at start when no path est sort the arr
        if path is None:
            nums.sort()
            path=[]

        res=[list(path)]

        for i in range(len(nums)):
            #core logic to ensure no duplicate subset
            if i>0 and nums[i]==nums[i-1]:
                continue

            path.append(nums[i])
            #passes sliced array so no already used elemnts come only remaining elements are used in next step
            res.extend(self.subsetsWithDup(nums[i+1:],path))
            #pop nums[i] resets the state so next i=num can be checked
            path.pop()
        return res
