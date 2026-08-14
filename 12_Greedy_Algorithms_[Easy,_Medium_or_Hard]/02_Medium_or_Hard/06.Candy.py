#https://leetcode.com/problems/candy/

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n  # Fix 1: Initialize array of length n with 1s

        # Pass 1: Left to Right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Pass 2: Right to Left
        for i in range(n - 2, -1, -1):  # Fix 2: Start from n - 2
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
