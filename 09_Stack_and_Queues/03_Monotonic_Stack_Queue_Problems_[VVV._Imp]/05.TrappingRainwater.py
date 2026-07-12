#https://leetcode.com/problems/trapping-rain-water/description/

class Solution:
    def trap(self, height: List[int]) -> int:
        #if list is empty
        if not height:
            return 0
        left,right=0,len(height)-1
        lmax,rmax=height[left],height[right]
        water=0#accumulate total units of trapped water

        #keeps running as long as left pointer hasnt met/crossed right ptr
        while left<right:
            if lmax<rmax:
                left+=1
                lmax=max(lmax,height[left])
                water+=lmax-height[left]
            else:#if rmax<=lmax process the right ptr
                right-=1
                rmax=max(rmax,height[right])
                water+=rmax-height[right]
        return water
