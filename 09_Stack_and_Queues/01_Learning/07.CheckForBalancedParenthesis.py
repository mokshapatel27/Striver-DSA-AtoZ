#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their corresponding opening brackets
        brackets_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in brackets_map:
                # If stack is empty or top doesn't match, it's invalid
                if not stack or stack[-1] != brackets_map[char]:
                    return False
                stack.pop()
            else:
                # It's an opening bracket, push to stack
                stack.append(char)
                
        # If stack is empty, all brackets were matched correctly
        return len(stack) == 0
