# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/

from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        # Sliding window + frequency counter
        # use a sliding window of length len(s1) on s2 

        if len(s1)>len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter() # this counter will be used to count the characters inside each window of length len(s1) inside s2

        for i in range(len(s2)):
            window_count[s2[i]]+=1 
         
         # exceed the window length(window becomes longer than s1)-> delete the character on the left 
            if i>=len(s1):
                left_char = s2[i-len(s1)]
                window_count[left_char]-=1
                # if the character count becomes 0, remove it from the counter, so it looks exactly like s1_count when i compare them
                if window_count[left_char]==0:
                    del window_count[left_char]

                
            if window_count == s1_count:
                return True

        return False

           

            
        
        
