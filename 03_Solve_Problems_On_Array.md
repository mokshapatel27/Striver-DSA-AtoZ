# 03 — Solve Problems on Arrays

> **Sheet:** Striver DSA A to Z  
> **Topic:** Arrays  
> **Language:** Python

---

## 1. Largest Element in Array

[🔗 GeeksforGeeks](https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1)

```python
class Solution:
    def largest(self, arr):
        return max(arr)
```

---

## 2. Second Largest Element

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

## 3. Check if Array Is Sorted and Rotated

[🔗 LeetCode](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/)

```python
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        x = len(nums)

        for i in range(x):
            if nums[i] > nums[(i + 1) % x]:
                count += 1

        return count <= 1
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

## 5 & 6. Rotate Array

[🔗 LeetCode](https://leetcode.com/problems/rotate-array/description/)

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
```

---

## 7. Move Zeroes

[🔗 LeetCode](https://leetcode.com/problems/move-zeroes/description/)

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_pos = 0

        for current in range(len(nums)):
            if nums[current] != 0:
                nums[non_zero_pos], nums[current] = nums[current], nums[non_zero_pos]
                non_zero_pos += 1
```

---

## 8. Search an Element in an Array

[🔗 GeeksforGeeks](https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1)

```python
class Solution:
    def search(self, arr, x):
        if x in arr:
            return arr.index(x)
        else:
            return -1
```

---

## 9. Union of Two Sorted Arrays

[🔗 GeeksforGeeks](https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1)

> **Note:** Two-pointer method left as practice.

```python
class Solution:
    def findUnion(self, a, b):
        return sorted(set(a) | set(b))
```

---

## 10. Missing Number

[🔗 LeetCode](https://leetcode.com/problems/missing-number/description/)

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        exp_sum = n * (n + 1) // 2
        actual = sum(nums)
        return exp_sum - actual
```

---

## 11. Max Consecutive Ones

[🔗 LeetCode](https://leetcode.com/problems/max-consecutive-ones/submissions/2021515727/)

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_ctr = 0
        max_ctr = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 1:
                current_ctr += 1
                if current_ctr > max_ctr:
                    max_ctr = current_ctr
            else:
                current_ctr = 0

        return max_ctr
```

---

## 12. Single Number

[🔗 LeetCode](https://leetcode.com/problems/single-number/description/)

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
```

---

## 13. Longest Subarray with Sum K

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
