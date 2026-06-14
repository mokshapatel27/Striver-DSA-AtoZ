#https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If we are ascending, the peak is on the right side
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # If we are descending, the peak is on the left side (including mid)
            else:
                right = mid
                
        return left 

        
