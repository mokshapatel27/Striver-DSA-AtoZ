#https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ptriangle=[]
        for i in range(numRows):
            row=[1]*(1+i)

            for j in range(1,i):
                row[j]=ptriangle[i-1][j-1]+ptriangle[i-1][j]
            ptriangle.append(row)
        return ptriangle


        
