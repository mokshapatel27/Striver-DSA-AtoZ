#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        # We loop while low < high because we want to narrow down the search space 
        # to a single element, which will be our minimum.
        while low < high:
            mid = (low + high) // 2
            
            # If the middle element is greater than the highest element,
            # the minimum must be in the right unsorted part.
            if nums[mid] > nums[high]:
                low = mid + 1
            # Otherwise, the minimum is in the left part (and could include mid).
            else:
                high = mid
                
        # When low == high, they point to the minimum element.
        return nums[low]
