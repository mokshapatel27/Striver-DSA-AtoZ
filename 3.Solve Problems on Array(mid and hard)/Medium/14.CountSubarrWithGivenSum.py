#https://leetcode.com/problems/subarray-sum-equals-k/description/ LEFT

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Dictionary to store the frequency of prefix sums
        # Base case: a prefix sum of 0 has occurred 1 time (before we start)
        prefix_sums = {0: 1}
        
        current_sum = 0
        total_subarrays = 0
        
        for num in nums:
            # Update the running prefix sum
            current_sum += num
            
            # Check if (current_sum - k) exists in our history
            if (current_sum - k) in prefix_sums:
                total_subarrays += prefix_sums[current_sum - k]
            
            # Record the current_sum in the dictionary
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return total_subarrays
