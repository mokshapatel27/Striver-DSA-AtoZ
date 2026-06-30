#https://leetcode.com/problems/divide-two-integers/
#O((\log N)^2),O(1)

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 1. Handle overflow case edge case up front
        # -2^31 / -1 = 2^31, which overflows 32-bit signed integer (max is 2^31 - 1)
        INT_MIN, INT_MAX = -2147483648, 2147483647

        if dividend==INT_MIN and divisor==-1:
            return INT_MAX
        neg=(dividend<1)^(divisor<1)
        absdividend=abs(dividend)
        absdivisor=abs(divisor)
        quotient=0
        # 4. Exponential search / Bit shift subtraction
        while absdividend>=absdivisor:
            tempdivisor=absdivisor
            multiple=1

            # Double the divisor and the multiple as long as it fits in the remaining dividend
            while absdividend>=(tempdivisor<<1):
                tempdivisor<<=1
                multiple<<=1

            absdividend-=tempdivisor
            quotient+=multiple
        
        return -quotient if neg else quotient

        
