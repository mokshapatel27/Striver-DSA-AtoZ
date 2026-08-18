#https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/2111514036/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    
        result = []
        stack = []
        curr = root
        last_visited = None
        
        while curr or stack:
            # 1. Reach the leftmost node
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                peek = stack[-1]
                # 2. If right child exists and hasn't been visited yet, move right
                if peek.right and last_visited != peek.right:
                    curr = peek.right
                # 3. Otherwise, process the current node
                else:
                    result.append(peek.val)
                    last_visited = stack.pop()
                    
        return result
        
        '''if not root:
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

        return [node.val for node in reversed(st2)]'''
