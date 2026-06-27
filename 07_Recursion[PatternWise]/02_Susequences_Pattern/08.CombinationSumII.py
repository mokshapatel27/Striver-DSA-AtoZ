#https://leetcode.com/problems/combination-sum-ii/description/

#LEFT

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        # Stack stores tuples of: (current_index, remaining_target, current_path)
        stack = [(0, target, [])]
        
        while stack:
            start, curr_target, path = stack.pop()
            
            if curr_target == 0:
                res.append(path)
                continue
                
            for i in range(start, len(candidates)):
                # Pruning: if the number is greater than the needed target, stop
                if candidates[i] > curr_target:
                    break
                
                # Skip duplicate elements at the same decision level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Push the next state onto the stack
                stack.append((i + 1, curr_target - candidates[i], path + [candidates[i]]))
                
        return res
