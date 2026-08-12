#https://leetcode.com/problems/task-scheduler/submissions/2104445089/

from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count task frequencies
        freq = Counter(tasks)
        max_freq = max(freq.values())
        
        # Step 2: Count how many tasks have the maximum frequency
        max_count = sum(1 for count in freq.values() if count == max_freq)
        
        # Step 3: Calculate required slots based on max frequency tasks
        ans = (max_freq - 1) * (n + 1) + max_count
        
        # Step 4: The answer is at least the total number of tasks
        return max(len(tasks), ans)
