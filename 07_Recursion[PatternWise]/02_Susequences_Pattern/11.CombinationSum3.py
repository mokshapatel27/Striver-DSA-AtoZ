#https://leetcode.com/problems/combination-sum-iii/description/

class Solution:
    def combinationSum3(self, k: int, n: int,path:List =None,start: int=1) -> List[List[int]]:
        if path is None:
            path=[]

        if len(path)==k and n==0:
            return [list(path)]
        if len(path)>=k and n<0:
            return []

        res=[]

        for i in range(start,10):
            path.append(i)
            res.extend(self.combinationSum3(k,n-i,path,i+1))
            path.pop()

        return res
