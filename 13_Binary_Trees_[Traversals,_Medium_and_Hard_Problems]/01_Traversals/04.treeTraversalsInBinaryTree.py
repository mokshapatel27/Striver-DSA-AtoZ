#https://www.naukri.com/code360/problems/tree-traversal_981269?leftPanelTabValue=SUBMISSION

def getTreeTraversal(root):
    if not root:
        return [],[],[]

    inorder,preorder,postorder=[],[],[]
    stack=[[root,1]]

    while stack:
        it=stack[-1]

        #preorder
        if it[1]==1:
            preorder.append(it[0].data)
            it[1]+=1
            if it[0].left:
                stack.append([it[0].left,1])
        elif it[1]==2:
            
            inorder.append(it[0].data)
            it[1]+=1
            if it[0].right:
                stack.append([it[0].right,1])
        else:
            postorder.append(it[0].data)
            stack.pop()

    return [inorder,preorder,postorder]
