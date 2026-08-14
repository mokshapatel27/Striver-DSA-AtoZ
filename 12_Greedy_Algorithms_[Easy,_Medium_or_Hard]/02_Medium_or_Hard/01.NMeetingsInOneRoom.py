#https://www.geeksforgeeks.org/problems/activity-selection-1587115620/1

class Solution:
    def activitySelection(self, start: list[int], finish: list[int]) -> int:
        
        # Step 1: Pair start and finish times together
        activities = list(zip(start, finish))
        p 2: Sort activities based on finish time
        activi
        # Steties.sort(key=lambda x: x[1])
        
        count = 0
        last_finish_time = -1
        
        # Step 3: Iterate through sorted activities
        for s, f in activities:
            # Selected activity must start strictly after the previous one finishes
            if s > last_finish_time:
                count += 1
                last_finish_time = f  # Update the finish time of last chosen activity
                
        return count
