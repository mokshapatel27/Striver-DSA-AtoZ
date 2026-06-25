#https://www.geeksforgeeks.org/problems/generate-all-binary-strings/1

class Solution:
    def binstr(self, n):
        
        return [format(i,f'0{n}b') for i in range(1<<n)]

'''2. f'0{n}b'
What it does: Dynamically constructs the format specification string.

How it works: It uses an f-string to plug the value of n into the format rule. If n = 3, this string becomes '03b'.

What '03b' means:

b: Convert the number to a binary string.

3: Ensure the output has a minimum width of 3 characters.

0: Pad any empty leading spaces with zeros.'''
