#https://www.geeksforgeeks.org/problems/infix-to-prefix-notation/1
#LEFT

class Solution:
    def infixToPrefix(self, s: str) -> str:
        # Step 1: Reverse string and swap brackets
        reversed_s = []
        for char in reversed(s):
            if char == '(':
                reversed_s.append(')')
            elif char == ')':
                reversed_s.append('(')
            else:
                reversed_s.append(char)
        
        # Step 2: Custom Postfix Conversion
        def get_precedence(op):
            if op in ('+', '-'): return 1
            if op in ('*', '/'): return 2
            if op == '^': return 3
            return 0

        result = []
        stack = []

        for char in reversed_s:
            # If operand, add to result
            if char.isalnum():
                result.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop() # Remove '('
            else:
                # Operator encountered
                # Critical Tweak for Associativity when reversed:
                # For ^ (right-to-left), pop if equal precedence.
                # For +, -, *, / (left-to-right), pop only if strictly greater precedence.
                while stack and (get_precedence(stack[-1]) > get_precedence(char) or 
                                (get_precedence(stack[-1]) == get_precedence(char) and char == '^')):
                    result.append(stack.pop())
                stack.append(char)

        while stack:
            result.append(stack.pop())

        # Step 3: Reverse the final result to get Prefix
        return "".join(reversed(result))
