#https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1 LEFT

class Solution:
    def inversionCount(self, arr):
        # Helper function to perform merge sort and count inversions
        def merge_sort_and_count(left, right):
            count = 0
            if left < right:
                mid = (left + right) // 2
                
                # Count inversions in left half, right half, and during merge
                count += merge_sort_and_count(left, mid)
                count += merge_sort_and_count(mid + 1, right)
                count += merge(left, mid, right)
                
            return count

        # Helper function to merge two sorted halves and count cross-inversions
        def merge(left, mid, right):
            left_part = arr[left : mid + 1]
            right_part = arr[mid + 1 : right + 1]
            
            i = j = 0
            k = left
            inv_count = 0
            
            # Merge the two temporary arrays back into arr[]
            while i < len(left_part) and j < len(right_part):
                if left_part[i] <= right_part[j]:
                    arr[k] = left_part[i]
                    i += 1
                else:
                    # Inversion found!
                    arr[k] = right_part[j]
                    inv_count += (len(left_part) - i)
                    j += 1
                k += 1
                
            # Copy remaining elements of left_part, if any
            while i < len(left_part):
                arr[k] = left_part[i]
                i += 1
                k += 1
                
            # Copy remaining elements of right_part, if any
            while j < len(right_part):
                arr[k] = right_part[j]
                j += 1
                k += 1
                
            return inv_count

        return merge_sort_and_count(0, len(arr) - 1)
