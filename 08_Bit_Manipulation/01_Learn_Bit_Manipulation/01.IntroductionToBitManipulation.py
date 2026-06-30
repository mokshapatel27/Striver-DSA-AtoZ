#https://www.geeksforgeeks.org/problems/bit-manipulation-1666686020/1

class Solution:
    def bitManipulation(self, num, i):
        #starts count from 1 instead of 0
        shift=i-1
        
        #shifts to a very right and only reads that bit
        get=(num>>shift)&1
        #OR forces chosen switch to turn ON keeping the rest of switches as it is
        setbit=num|(1<<shift)#brand new switch which is turned on at out exact position
        #~ is a flipflop it turns the switch off
        clearbit=num&~(1<<shift)
        
        print(f"{get} {setbit} {clearbit}")
