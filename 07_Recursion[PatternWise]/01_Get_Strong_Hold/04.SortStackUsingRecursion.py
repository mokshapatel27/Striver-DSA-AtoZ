#https://www.geeksforgeeks.org/problems/sort-a-stack/1

class Solution:
    def sortStack(self, st):
        tmp_st=[]
        
        while st:
            tmp=st.pop()
            
            #run this till the top of temp stack isnt greater than temp var, this adds the var from temp stack back to og stack till cond isnt satisfied
            while tmp_st and tmp_st[-1]<tmp:
                st.append(tmp_st.pop())
            #runs when condition satisfied i.e when top temp st>temp var 
            tmp_st.append(tmp)
        
        while tmp_st:
            st.append(tmp_st.pop())
