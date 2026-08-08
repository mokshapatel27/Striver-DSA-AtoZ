#https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/submissions/2098373864/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = {'a': -1, 'b': -1, 'c': -1}
        ans = 0

        for i, char in enumerate(s):
            last[char] = i
            
            # Check if all 'a', 'b', and 'c' have appeared at least once
            if last['a'] != -1 and last['b'] != -1 and last['c'] != -1:
                ans += min(last['a'], last['b'], last['c']) + 1

        return ans
