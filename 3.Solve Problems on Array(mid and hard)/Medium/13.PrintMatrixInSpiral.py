#https://leetcode.com/problems/spiral-matrix/description/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        left,right=0,len(matrix[0])-1
        top,bottom=0,len(matrix)-1

        while left<=right and top<=bottom:
            res.extend(matrix[top][i] for i in range(left,right+1))
            top+=1

            res.extend(matrix[i][right] for i in range(top,bottom+1))
            right-=1

            if top<=bottom:
                res.extend(matrix[bottom][i] for i in range(right,left-1,-1))
                bottom-=1

            if left<=right:
                res.extend(matrix[i][left] for i in range(bottom,top-1,-1))
                left+=1
        return res
