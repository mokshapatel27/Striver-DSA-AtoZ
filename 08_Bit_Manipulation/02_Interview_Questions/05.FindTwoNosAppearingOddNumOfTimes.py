#https://www.geeksforgeeks.org/problems/two-numbers-with-odd-occurrences5846/1


class Solution:
    def twoOddNum(self, arr):
        # Step 1: XOR all elements. 
        # Elements appearing even times cancel out, leaving xor_sum = x ^ y
        xor_sum = 0
        for num in arr:
            xor_sum ^= num
            
        # Step 2: Find the rightmost set bit of xor_sum
        # This bit is different between the two odd-occurring numbers
        set_bit = xor_sum & -xor_sum
        
        # Step 3: Divide numbers into two groups based on the set bit
        num1, num2 = 0, 0
        for num in arr:
            if num & set_bit:
                num1 ^= num
            else:
                num2 ^= num
                
        # Return the numbers in decreasing order
        return [num1, num2] if num1 > num2 else [num2, num1]
