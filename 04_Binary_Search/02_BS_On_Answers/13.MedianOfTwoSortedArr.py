#https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/2032668492/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to achieve O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half_len = (m + n + 1) // 2
        
        while low <= high:
            # Partition positions
            i = (low + high) // 2
            j = half_len - i
            
            # Edge cases: handling out-of-bounds with infinity
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            
            # Check if we found the correct partition
            if left1 <= right2 and left2 <= right1:
                # If total number of elements is odd
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                # If total number of elements is even
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
            
            elif left1 > right2:
                # We are too far right in nums1, move left
                high = i - 1
            else:
                # We are too far left in nums1, move right
                low = i + 1
                
        return 0.0
