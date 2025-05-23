# 344. Reverse String
# https://leetcode.com/problems/reverse-string/

class Solution(object):
    def reverseString(self, s):
        # Two Pointers 
        left, right = 0, len(s)-1
        while left<right:
            s[left],s[right] = s[right],s[left]
            left+=1
            right-=1
        return s
            # if i want to return s as a string : return ''.join(s)