#https://www.geeksforgeeks.org/problems/odd-or-even3618/1
#O(1)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #Cleverly clears the lowest set bit. If there was only one set bit to begin with (which is true for all powers of two), the result becomes 0.
        return n>0 and (n &(n-1))==0
