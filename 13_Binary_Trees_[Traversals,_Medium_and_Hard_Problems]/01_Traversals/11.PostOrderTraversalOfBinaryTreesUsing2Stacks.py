#https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        st1=[root]
        st2=[]

        while st1:
            node=st1.pop()
            st2.append(node)

            if node.left:
                st1.append(node.left)
            if node.right:
                st1.append(node.right)

        return [node.val for node in reversed(st2)]
