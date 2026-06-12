#https://www.geeksforgeeks.org/problems/maximum-sub-array5443/1

class Solution:
    def findSubarray(self, arr):
        current=0
        maximum=-1
    	start=-1
    	end=-1
    	temp_start=0
    	
    	for i in range(len(arr)):
    	    num=arr[i]
    	    if num<0:
    	        current=0
    	        temp_start=i+1
    	        continue
    	    current=current+num
    	    
    	    if current>maximum:
    	        maximum=current
    	        start=temp_start
    	        end=i
            elif current==maximum:
                if(i-temp_start)>(end-start):
                    start=temp_start
                    end=i
                    
        if start==-1:
            return[-1]
            
        return arr[start:end+1]
        
