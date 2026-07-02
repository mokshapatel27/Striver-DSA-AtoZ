#https://www.geeksforgeeks.org/problems/all-divisors-of-a-number/1

class Solution:
    def getDivisors(self, n):
        left_divisors = []
        right_divisors = []
        
        # Iterate up to square root of n
        i = 1
        while i * i <= n:
            if n % i == 0:
                left_divisors.append(i)
                # Avoid duplicating the square root (e.g., 4*4 = 16)
                if i * i != n:
                    right_divisors.append(n // i)
            i += 1
            
        # Since right_divisors are collected from largest to smallest,
        # reverse them to maintain ascending order when combining.
        return left_divisors + right_divisors[::-1]
