#https://www.geeksforgeeks.org/problems/set-the-rightmost-unset-bit4436/1

class Solution:
    def setBit(self, n):
        return n|(n+1)
    '''Why this works:Adding 1 to $n$ flips all the trailing 1s (from right to left) to 0s,
    and flips the rightmost 0 (the first unset bit) to 1.
    Performing a bitwise OR (|) between the original number $n$ and $n + 1$ preserves all original
    set bits while switching that rightmost 0 to a 1.'''
