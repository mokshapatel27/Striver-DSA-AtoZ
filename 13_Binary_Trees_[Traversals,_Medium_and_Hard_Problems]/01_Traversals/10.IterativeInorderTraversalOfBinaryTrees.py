#https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        stack=[]
        curr=root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            result.append(curr.val)

            curr=curr.right
        return result
        
        '''result=[]

        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(root)
        return result'''
