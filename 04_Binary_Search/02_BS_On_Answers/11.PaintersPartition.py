#https://www.naukri.com/code360/problems/painter-s-partition-problem_1089557?leftPanelTabValue=SUBMISSION

def findLargestMinDistance(boards: list, k: int) -> int:
    # The minimum possible max time is the length of the largest single board
    # The maximum possible max time is the sum of all board lengths
    low = max(boards)
    high = sum(boards)
    ans = high

    while low <= high:
        mid = (low + high) // 2
        
        # Inline validation: Check if 'mid' is a valid maximum time limit
        painters_used = 1
        current_board_sum = 0
        
        for board in boards:
            if current_board_sum + board <= mid:
                current_board_sum += board
            else:
                # Assign to a new painter
                painters_used += 1
                current_board_sum = board
        
        # If the boards can be painted within 'mid' time using <= k painters
        if painters_used <= k:
            ans = mid        # 'mid' is a feasible solution; record it
            high = mid - 1   # Try to find a smaller maximum time
        else:
            low = mid + 1    # 'mid' is too small; we need more time
            
    return ans
