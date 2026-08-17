#https://www.geeksforgeeks.org/problems/binary-tree-representation/1

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, nodes):
        if not nodes:
            return None
            
        def helper(i):
            if i>=len(nodes):
                return None
            root=Node(nodes[i])
            
            root.left=helper(2*i+1)
            root.right=helper(2*i+2)
            
            return root
            
        return helper(0)
        
    
        
