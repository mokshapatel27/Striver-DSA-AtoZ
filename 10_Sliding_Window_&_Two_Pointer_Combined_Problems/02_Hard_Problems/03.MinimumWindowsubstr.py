#https://leetcode.com/problems/minimum-window-substring/
#LEFT

class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        # Step 1: Count target character frequencies manually
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        # Unique characters in t that need to be satisfied
        need = len(t_count)
        have = 0

        # Dictionary to keep track of character counts in current window
        window = {}

        # Track the minimum window [length, left_index, right_index]
        res = [float("inf"), 0, 0]
        left = 0

        # Step 2: Expand the right pointer to find valid window
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # If current char count matches required count in t, increment have
            if char in t_count and window[char] == t_count[char]:
                have += 1

            # Step 3: Try shrinking from left when window contains all required characters
            while have == need:
                # Update our minimum window result
                window_size = right - left + 1
                if window_size < res[0]:
                    res = [window_size, left, right]

                # Pop left character from window
                left_char = s[left]
                window[left_char] -= 1

                # If removing left_char invalidates the requirement, decrement have
                if (
                    left_char in t_count
                    and window[left_char] < t_count[left_char]
                ):
                    have -= 1

                left += 1

        # Step 4: Return result substring or empty string if no valid window found
        min_len, min_l, min_r = res
        return s[min_l : min_r + 1] if min_len != float("inf") else ""
