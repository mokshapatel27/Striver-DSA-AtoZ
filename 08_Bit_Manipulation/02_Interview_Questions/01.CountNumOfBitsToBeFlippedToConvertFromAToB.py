#https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        #applies xor between start and goal
        xor=start^goal
        count=0
        #loop which works until all set bits are covered
        while xor>0:
            #Brian Kernighan’s Algorithm.Subtracting 1 from a binary number flips all the bits from the rightmost 1 to the end. When you bitwise AND (&) the original number with this subtracted number, it completely clears (turns to 0) the lowest set bit.
            xor &=(xor-1)
            count+=1
        return count
