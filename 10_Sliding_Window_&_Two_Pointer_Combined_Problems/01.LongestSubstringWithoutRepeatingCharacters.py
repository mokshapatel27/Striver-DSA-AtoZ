#https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/2096708430/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #len=right-left+1
        charmap={}
        left=0 #starting pos
        maxlen=0 #stores longest valid length so far

        for right, char in enumerate(s): #moves right ptr index by index from start to end
        #checks for duplicates
            if char in charmap and charmap[char]>=left:
                left=charmap[char]+1 #move idx of left from duplicate letter forward

            charmap[char]=right #Updates (or adds) the entry for char in the dictionary so its value becomes the current index right.
            maxlen=max(maxlen,right-left+1)#Compares the length of our current window against the biggest valid length found so far
        return maxlen
