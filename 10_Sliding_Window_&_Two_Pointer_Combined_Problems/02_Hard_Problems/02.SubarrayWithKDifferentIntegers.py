#https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atMostK(k: int) -> int:
            count = {}
            left = 0
            ans = 0
            
            for right in range(len(nums)):
                # Expand window by adding nums[right]
                count[nums[right]] = count.get(nums[right], 0) + 1
                
                # Shrink window if distinct elements exceed k
                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                
                # Number of valid subarrays ending at 'right'
                ans += right - left + 1
                
            return ans

        return atMostK(k) - atMostK(k - 1)
