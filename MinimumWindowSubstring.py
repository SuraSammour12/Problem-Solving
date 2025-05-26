# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter  
class Solution(object):
    def minWindow(self, s, t):
        # Sliding Window : variable window
        if not s or not t :
            return ""

        t_count = Counter(t)  # Counts the letters in word t, and how many times each one appears
        formed = 0  # how many I have matched so far, start from 0
        required = len(t_count)  # how many different letters I need

        # Set up the sliding window 
        left = 0
        window_counts = {}
        min_len = float('inf')
        min_window = (0,0)
        # use a window to look at parts of s, left is the start of the window 
        # window_counts: tracks the letters inside the window
        # min_len: remembers the shortest match I find
        # min_window: keeps the best start and end positions

        # slide the window from the left to right 
        for right in range(len(s)):
            char = s[right]  # add current letter into the window
            window_counts[char] = window_counts.get(char, 0) + 1  # count how many times I've seen it 

            # check if I matched one required letter
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1

            # shrinking the window from the left => if I matched all the letters I need, try to make window smaller 
            while left <= right and formed == required:
                # save this as the best window (if smaller)
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    min_window = (left, right)

                # remove letter from the left => shrinking
                left_char = s[left]
                window_counts[left_char] -= 1 

                # check if I lost a needed match 
                if left_char in t_count and window_counts[left_char] < t_count[left_char]:
                    formed -= 1
                # move the window's left side to the right 
                left += 1

        # return the result
        start, end = min_window  
        return s[start:end+1] if min_len != float("inf") else ""
        # if I found a matching window, return it. If not, return an empty string
