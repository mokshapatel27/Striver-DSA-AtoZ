#https://www.geeksforgeeks.org/problems/the-celebrity-problem/1

class Solution:
    def celebrity(self, mat):
        n=len(mat)
        
        top=0
        down=n-1
        
        while top<down: #loops till top and bottom are two diff ppl
            if mat[top][down]==1:#top knows down it cant be a celebrity
                top+=1
            else:#top doesnt know down down cant be celebrity
                down-=1
                
        #when loop ends top and down points at sme index which is celebrity
        candidate=top
        
        for i in range(n):
            if i!=candidate:
                #candidate knows the person or the person doesnt know the candidate invalid
                if mat[candidate][i]==1 or mat[i][candidate]==0:
                    return -1
                    
        return candidate
