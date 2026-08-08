#https://www.geeksforgeeks.org/problems/minimum-window-subsequence/1

class Solution:

  def minWindow(self, s1: str, s2: str) -> str:
    n, m = len(s1), len(s2)
    i, j = 0, 0
    min_len = float("inf")
    start_idx = -1

    while i < n:
      # Step 1: Forward match s2 in s1
      if s1[i] == s2[j]:
        j += 1

        # Found all characters of s2 in order
        if j == m:
          end = i  # Right boundary of current valid window
          j -= 1

          # Step 2: Backward scan to find the optimal left boundary
          while j >= 0:
            if s1[i] == s2[j]:
              j -= 1
            i -= 1

          i += 1  # Left boundary of current valid window
          j = 0  # Reset s2 pointer for the next window

          # Step 3: Update minimum length window
          if (end - i + 1) < min_len:
            min_len = end - i + 1
            start_idx = i

      i += 1

    return "" if start_idx == -1 else s1[start_idx : start_idx + min_len]
