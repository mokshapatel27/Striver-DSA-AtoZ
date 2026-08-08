#https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        
        # Step 1: Take the first k cards from the left
        current_sum = 0
        for i in range(k):
            current_sum += cardPoints[i]
            
        max_sum = current_sum
        
        # Step 2: Swap left cards with right cards one by one
        for i in range(k):
            current_sum -= cardPoints[k - 1 - i]      # Remove card from left
            current_sum += cardPoints[n - 1 - i]      # Add card from right
            if current_sum > max_sum:
                max_sum = current_sum
                
        return max_sum
