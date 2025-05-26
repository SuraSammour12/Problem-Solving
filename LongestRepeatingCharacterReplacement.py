# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict
class Solution(object):
    # Variable sliding window
    def characterReplacement(self, s, k):
        count = defaultdict(int) # holds the frequency of letters in current window
        left = 0
        max_len = 0 # result : longest window found
        max_freq = 0 # frequency of the most common letter in the window

        for right in range(len(s)):
            count[s[right]]+=1 # add current char to the window
            max_freq = max(max_freq, count[s[right]]) 

            # if more than k chars need to be replaced => shrink the window (from left side)
            # Number of changes required = Window size - Number of most frequent characters within the window
            while (right-left+1)-max_freq > k:
                count[s[left]]-=1 # remove the leftmost char from the window
                left+=1

            max_len = max(max_len, right-left+1) 

        return max_len 


       

       
        