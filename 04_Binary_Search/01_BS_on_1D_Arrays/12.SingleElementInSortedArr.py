#https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low,high=0,len(nums)-1

        while low<high:
            mid=(low+high)//2
            #if paired elements are placed where theyre supposed tobe single element is in right half
            if nums[mid]==nums[mid^1]:
                low=mid+1
            else:#otherwise its in the left half
                high=mid
        return nums[low]
