#https://leetcode.com/problems/word-break/submissions/2048090159/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True

        for word in wordDict:
            if s.startswith(word):
                if self.wordBreak(s[len(word):],wordDict):
                    return True
                else:
                    return False
