#https://www.geeksforgeeks.org/problems/count-subarray-with-given-xor/1

class Solution:
    def subarrayXor(self, arr, k):
     \
        # Hash map to store (prefix_xor -> frequency)
        xor_map = {}
        # Base case: an empty prefix has a cumulative XOR of 0, seen 1 time
        xor_map[0] = 1
        
        count = 0
        current_xor = 0
        
        for val in arr:
            # Update the cumulative prefix XOR
            current_xor ^= val
            
            # Calculate what prefix XOR we need to find to get target k
            target_prefix = current_xor ^ k
            
            # If that target prefix XOR exists, add its frequency to our count
            if target_prefix in xor_map:
                count += xor_map[target_prefix]
                
            # Update the frequency of the current prefix XOR in the map
            if current_xor in xor_map:
                xor_map[current_xor] += 1
            else:
                xor_map[current_xor] = 1
                
        return count
