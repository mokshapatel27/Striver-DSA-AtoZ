#https://www.geeksforgeeks.org/problems/postorder-traversal/1

''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        res=[]
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.data)
            
        dfs(root)
        return res
        
        
