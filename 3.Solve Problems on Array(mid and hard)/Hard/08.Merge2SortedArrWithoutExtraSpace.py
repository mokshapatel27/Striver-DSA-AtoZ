#https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Set up three pointers
        p1 = m - 1      # Pointer for the last valid element in nums1
        p2 = n - 1      # Pointer for the last element in nums2
        p = m + n - 1   # Pointer for the very last position in nums1
        
        # Merge elements from right to left
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # Copy over any remaining elements from nums2
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
