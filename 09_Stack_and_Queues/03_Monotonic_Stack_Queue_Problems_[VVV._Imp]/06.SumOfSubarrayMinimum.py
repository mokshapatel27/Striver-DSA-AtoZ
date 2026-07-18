#https://leetcode.com/problems/sum-of-subarray-minimums/
#LEFT 


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        '''-left choices=i-idx of prev smaller elements
        -right choices=idx of next smaller elements-i
        -total subarr for arr[i]=left*right choices'''

        MOD = 10**9 + 7
        # Pad with -infinity to automatically handle boundaries and flush the stack
        arr = [-float('inf')] + arr + [-float('inf')]
        stack = []
        total_sum = 0
        
        for i, val in enumerate(arr):
            # Maintain a monotonically increasing stack
            while stack and arr[stack[-1]] > val:
                mid = stack.pop()
                left = stack[-1]
                right = i
                
                # Count how many subarrays mid is the minimum for
                total_sum += arr[mid] * (mid - left) * (right - mid)
                
            stack.append(i)
            
        return total_sum % MOD

        


