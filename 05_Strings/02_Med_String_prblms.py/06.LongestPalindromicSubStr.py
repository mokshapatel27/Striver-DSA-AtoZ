#https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start=0
        maxlen=1

        for i in range(len(s)):
            left,right=i,i
            while left>=0 and right<len(s) and s[left]==s[right]:
                if(right-left+1)>maxlen:
                    start=left
                    maxlen=right-left+1
                left-=1
                right+=1

            left,right=i,i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                if(right-left+1)>maxlen:
                    start=left
                    maxlen=right-left+1
                left-=1
                right+=1
        return s[start: start+maxlen]
