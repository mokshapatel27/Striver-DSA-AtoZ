#https://www.geeksforgeeks.org/problems/prime-factorization-using-sieve/1

class Solution:

    def findPrimeFactors(self, N):
        # spf[i] will store the smallest prime factor of i
        spf = [i for i in range(N + 1)]

        # Standard Sieve to precompute SPF
        for i in range(2, int(N**0.5) + 1):
            if spf[i] == i:  # i is prime
                for j in range(i * i, N + 1, i):
                    if spf[j] == j:  # Mark only if not marked before
                        spf[j] = i

        # Logarithmic factorization using the precomputed SPF array
        factors = []
        while N > 1:
            factors.append(spf[N])
            N //= spf[N]

        return factors
