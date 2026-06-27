#https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target==0:return [[]]
        if target<0 or not candidates: return []

        include=[[candidates[0]]+ comb for comb in self.combinationSum(candidates,target-candidates[0])]

        exclude=self.combinationSum(candidates[1:],target)

        return include+exclude
