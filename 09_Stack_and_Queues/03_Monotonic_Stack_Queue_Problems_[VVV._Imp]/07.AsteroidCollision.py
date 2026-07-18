#https://leetcode.com/problems/asteroid-collision/
#O(N),O(N)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]

        for ast in asteroids:
            #last ast is moving to right and curr to left
            while stack and stack[-1]>0 and ast<0:
                diff=ast+stack[-1]

                #current left moving ast is bigger
                if diff<0:
                    stack.pop()
                #ast in stack is bigger
                elif diff>0:
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(ast)

        return stack
