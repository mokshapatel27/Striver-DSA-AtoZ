#https://leetcode.com/problems/count-primes/description/
#LEFT

class Solution:

    def countPrimes(self, n: int) -> int:
        #because no prime nos. smaller than 0&1
        if n <= 2:
            return 0

        # Create boolean arr and fill entirely with true
        is_prime = [True] * n
        #set 0&1 to False manually
        is_prime[0] = is_prime[1] = False

        # Start from 2 till rootN
        for i in range(2, int(n**0.5) + 1):
            #check if surrent element is stil marked True
            if is_prime[i]:
                # start,stop,skip
                is_prime[i * i : n : i] = [False] * len(
                    range(i * i, n, i)
                )

        return sum(is_prime)
