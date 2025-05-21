# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
class Solution(object):
    def isAnagram(self, s, t):
        
        if len(s) != len(t):
          return False
        count_s = {}
        count_t = {}

        for i in range(len(s)):
            count_s[s[i]] = 1+count_s.get(s[i],0)
            count_t[t[i]] = 1+count_t.get(t[i],0)
        return count_s==count_t
       


