#https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''a window is valid as long as: (right-left+1)-maxfreq<=k'''
        count={}
        left=0
        maxlen=0
        maxfreq=0

        for right in range(len(s)):
            #count.get(key,defaultval)
            #looks at the char pos in right and updates it in dict
            count[s[right]]=count.get(s[right],0)+1
            #checks if it is the most freq occuring
            maxfreq=max(maxfreq,count[s[right]])

            while (right-left+1)-maxfreq>k: #total window if >k window is invalid
                count[s[left]]-=1 #shrink the window
                left+=1

            maxlen=max(maxlen,right-left+1)

        return maxlen


