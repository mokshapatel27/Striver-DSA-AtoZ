#https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        else:
            return -1

            
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left = 0
#         right = len(nums) - 1
        
#         while left <= right:
#             # Find the middle index of the current search space
#             mid = (left + right) // 2
            
#             # Check if the target is found at the middle index
#             if nums[mid] == target:
#                 return mid
#             # If target is greater, ignore the left half
#             elif nums[mid] < target:
#                 left = mid + 1
#             # If target is smaller, ignore the right half
#             else:
#                 right = mid - 1
                
#         # If the target is not present in the array
#         return -1
