# 03 — Solve Problems on Arrays

> **Sheet:** Striver DSA A to Z  
> **Topic:** Arrays  
> **Language:** Python

---

## 1. Given an array arr[]. The task is to find the largest element and return it.

[🔗 GeeksforGeeks](https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1)

```python
class Solution:
    def largest(self, arr):
        return max(arr)
```

---

## 2. Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1. Note: The second largest element should not be equal to the largest element.

[🔗 GeeksforGeeks](https://www.geeksforgeeks.org/problems/second-largest3735/1)

```python
import heapq
class Solution:
    def getSecondLargest(self, arr):
        # Remove duplicates using set
        unique_elements = list(set(arr))
        # Find the 2 largest distinct elements
        twolargest = heapq.nlargest(2, unique_elements)
        # If we have fewer than 2 unique elements, return -1
        return twolargest[1] if len(twolargest) >= 2 else -1
```

---

## 3. Check if Array Is Sorted and Rotated.

[🔗 LeetCode](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/)

```python
class Solution:
    def check(self, nums: List[int]) -> bool:
        count=0
        x=len(nums)

        for i in range(x):
            if nums[i]>nums[(i+1)%x]:
                count+=1
        return count<=1
```

---

## 4. Remove Duplicates from Sorted Array

[🔗 LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        return len(nums)
```

---

## 5/6. Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

[🔗 LeetCode](https://leetcode.com/problems/rotate-array/description/)

```python
# class Solution:
#         def rotate(self, nums: List[int], k: int) -> None:
#                 n=len(nums)
#                         k=k%n
#                              nums[:]=nums[-k:]+nums[:-k]

class Solution:
    def rotate(self,nums:list[int],k:int)-> None:
        n=len(nums)
        k=k%n

        def reverse(start:int,end:int)->None:
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
```

---

## 7. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in-place without making a copy of the array.

[🔗 LeetCode](https://leetcode.com/problems/move-zeroes/description/)

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_pos=0

        for current in range(len(nums)):
            if nums[current]!=0:
                nums[non_zero_pos],nums[current]=nums[current],nums[non_zero_pos]

                non_zero_pos+=1
```

---

## 8. Given an array, arr[] of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.

[🔗 GeeksforGeeks](https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1)

```python
class Solution:
    def search(self, arr, x):
        
        if x in arr:
            return arr.index(x)
        else:
                 return -1

# class Solution:
#     def search(self, arr, x):
#         for i, num in enumerate(arr):
#             if num == x:
#                 return i  # Returns the index of the first occurrence
#         return -1  # Returns -1 if the loop finishes and x isn't found
```

---

## 9. Given two sorted arrays a[] and b[], where each array may contain duplicate elements, the task is to return the elements in the union of the two arrays in sorted order. Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays. (two-ptr method left)

[🔗 GeeksforGeeks](https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1)

```python
class Solution:
    def findUnion(self, a, b):
        return sorted(set(a)|set(b))
```

---

## 10. Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

[🔗 LeetCode](https://leetcode.com/problems/missing-number/description/)

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        exp_sum=n*(n+1)//2
        actual=sum(nums)
        return exp_sum-actual
```

---

## 11. Given a binary array nums, return the maximum number of consecutive 1's in the array.

[🔗 LeetCode](https://leetcode.com/problems/max-consecutive-ones/submissions/2021515727/)

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_ctr=0
        max_ctr=0
        n=len(nums)
        for i in range(n):
            if nums[i]==1:
                current_ctr+=1

                if current_ctr>max_ctr:
                    max_ctr=current_ctr
            else:
                current_ctr=0
        return max_ctr
```

---

## 12. Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.

[🔗 LeetCode](https://leetcode.com/problems/single-number/description/)

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for num in nums:
            result^=num
        return result
```

---

## 13. Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.

[🔗 GeeksforGeeks](https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1)

```python
class Solution:
    def longestSubarray(self, arr, k):
        # 1. Initialize your tools
        sum_map = {}
        prefix_sum = 0
        max_len = 0
        
        # 2. Iterate through the array with both index and value
        for i, num in enumerate(arr):
            # Update the cumulative sum
            prefix_sum += num
            
            # 3. Check if the sum from the very beginning equals k
            if prefix_sum == k:
                max_len = i + 1
                
            # 4. Check if (prefix_sum - k) is in the map
            if (prefix_sum - k) in sum_map:
                max_len = max(max_len, i - sum_map[prefix_sum - k])
                
            # 5. Only store the prefix sum if it hasn't been seen before
            if prefix_sum not in sum_map:
                sum_map[prefix_sum] = i
                
        # 6. Return the maximum length found
        return max_len
```
