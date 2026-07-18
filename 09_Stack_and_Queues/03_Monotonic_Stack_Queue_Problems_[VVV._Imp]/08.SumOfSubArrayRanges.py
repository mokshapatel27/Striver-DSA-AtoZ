#https://leetcode.com/problems/sum-of-subarray-ranges/description/
#LEFT

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        
        def get_sum(is_max: bool) -> int:
            total = 0
            # Monotonic stack stores indices
            stack = []
            
            # Go up to n to clear out remaining elements in the stack at the end
            for i in range(n + 1):
                while stack and (i == n or (nums[stack[-1]] < nums[i] if is_max else nums[stack[-1]] > nums[i])):
                    mid = stack.pop()
                    # Determine left and right boundaries
                    left = stack[-1] if stack else -1
                    right = i
                    
                    # Number of subarrays where nums[mid] is the min/max
                    count = (mid - left) * (right - mid)
                    total += count * nums[mid]
                    
                stack.append(i)
            return total

        return get_sum(is_max=True) - get_sum(is_max=False)
