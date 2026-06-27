#https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str,path: List[str]=None,res: List[List[str]]=None) -> List[List[str]]:
        if path is None: path=[]
        if res is None: res=[]

        if not s: 
            res.append(list(path))
            return res
        for i in range(1,len(s)+1):
            prefix=s[:i]

            if prefix==prefix[::-1]:
                path.append(prefix)
                self.partition(s[i:],path,res)
                path.pop()

        return res
