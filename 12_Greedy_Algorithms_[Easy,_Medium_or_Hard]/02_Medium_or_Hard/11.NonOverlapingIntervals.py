#https://leetcode.com/problems/non-overlapping-intervals/submissions/2108738960/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort by end time
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        prev_end = intervals[0][1]
        
        # Check remaining intervals
        for i in range(1, len(intervals)):
            # If current interval starts before the previous one ends, it overlaps
            if intervals[i][0] < prev_end:
                count += 1  # Remove this interval
            else:
                prev_end = intervals[i][1]  # Keep it and update end time
                
        return count
