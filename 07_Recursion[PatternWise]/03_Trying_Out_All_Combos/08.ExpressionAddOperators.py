#https://leetcode.com/problems/expression-add-operators/
#UNDERSTANDING LEFT

class Solution:
    def addOperators(self, num: str, target: int, idx: int = 0, prev_operand: int = 0, current_val: int = 0, path: str = "") -> List[str]:
        # Base Case: If we have processed the entire string
        if idx == len(num):
            return [path] if current_val == target and path else []
        
        res = []
        
        # Explore all possible next numbers split from the remaining string
        for i in range(idx, len(num)):
            # Handle leading zero constraint: "0" is fine, but "05" is invalid
            if i > idx and num[idx] == '0':
                break
                
            part_str = num[idx:i+1]
            part_val = int(part_str)
            
            # If it's the very first number, we cannot prefix it with an operator
            if idx == 0:
                res.extend(self.addOperators(num, target, i + 1, part_val, part_val, part_str))
            else:
                # Case 1: Addition '+'
                res.extend(self.addOperators(num, target, i + 1, part_val, current_val + part_val, path + '+' + part_str))
                
                # Case 2: Subtraction '-'
                res.extend(self.addOperators(num, target, i + 1, -part_val, current_val - part_val, path + '-' + part_str))
                
                # Case 3: Multiplication '*'
                # Undo the previous addition/subtraction, apply multiplication precedence
                res.extend(self.addOperators(num, target, i + 1, prev_operand * part_val, (current_val - prev_operand) + (prev_operand * part_val), path + '*' + part_str))
                
        return res
