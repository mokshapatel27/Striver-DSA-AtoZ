#https://leetcode.com/problems/generate-parentheses/submissions/2046619550/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      #empty str openct,closect=0
        queue=[("",0,0)]

        for _ in range(2*n):
            nxtq=[]
            for s,openct,closect in queue:
              #if below condition means we still have pending open brackets append it t nxtq
                if openct<n:
                    nxtq.append((s+ "(",openct+1,closect))
                if closect<openct:
                    nxtq.append((s+ ")",openct,closect+1))
            queue=nxtq
        return [s for s,_,_ in queue]
