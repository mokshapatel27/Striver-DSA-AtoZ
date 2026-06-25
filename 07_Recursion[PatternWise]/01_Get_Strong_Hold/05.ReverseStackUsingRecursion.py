#https://www.geeksforgeeks.org/problems/reverse-a-stack/1

class Solution:
    def reverseStack(self, st):
        if not st:
            return 
        
        top=st.pop()

        self.reverseStack(st)
        
        st.insert(0,top)
