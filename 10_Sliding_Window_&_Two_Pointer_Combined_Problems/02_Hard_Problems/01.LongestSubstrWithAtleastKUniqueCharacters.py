#https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

class Solution:
    def longestKSubstr(self, s, k):
        freq={}
        left=0
        maxlen=-1
        
        for right in range(len(s)):
            char=s[right]
            freq[char]=freq.get(char,0)+1
            
            #shrink left side
            while len(freq)>k:
                leftchar=s[left]
                freq[leftchar]-=1
                if freq[leftchar]==0:
                    del freq[leftchar]
                left+=1
                
            if len(freq)==k:
                maxlen=max(maxlen,right-left+1)
                
        return maxlen
