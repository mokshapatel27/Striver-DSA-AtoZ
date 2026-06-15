#https://leetcode.com/problems/find-a-peak-element-ii/

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        lowc=0
        highc=len(mat[0])-1

        while lowc<=highc:
            midc=(lowc+highc)//2

            maxr=max(range(len(mat)), key=lambda r:mat[r][midc])

            lval=mat[maxr][midc-1] if midc-1>=0 else -1
            rval=mat[maxr][midc+1] if midc+1<len(mat[0]) else -1

            if mat[maxr][midc]> lval and mat[maxr][midc]>rval:
                return [maxr,midc]

            elif mat[maxr][midc]<rval:
                lowc=midc+1
            else:
                highc=midc-1
        return []
