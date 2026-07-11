#https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #decreasing stack stores numbers from nums2
        stack=[]
        #empty list acts as decreasing stack stores num from nums2 waiting to find greater element
        greater_map={}

        for num in nums2:
            #when stack is not empty and no. is > top element of stack
            while stack and num>stack[-1]:
                #pop from list add to stack
                greater_map[stack.pop()]=num
            stack.append(num)
        return [greater_map.get(num,-1) for num in nums1]
