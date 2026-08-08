#https://www.geeksforgeeks.org/problems/implementation-of-priority-queue-using-binary-heap/1

# 1. parent(i): Function to return the parent node of node i
# 2. leftChild(i): Function to return index of the left child of node i
# 3. rightChild(i): Function to return index of the right child of node i
# 4. shiftUp(int i): Function to shift up the node in order to maintain the
# heap property
# 5. shiftDown(int i): Function to shift down the node in order to maintain the
# heap property.
# int s=-1, current index value of the array H[].


class Solution:
    def extractMax(self):
        global H,s
        
        if s<0:
            return -1
        
        result=H[0]
            
        H[0]=H[s]
        s-=1
        
        i=0
        while True:
            left=2*i+1
            right=2*i+2
            largest=i
            
            if left<=s and H[left]>H[largest]:
                largest=left
                
            if right<=s and H[right]>H[largest]:
                largest=right
            if largest==i:
                break
            
            H[i],H[largest]=H[largest],H[i]
            
            i=largest
        return result
        
