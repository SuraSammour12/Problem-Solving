# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
     if x<0:
        return False
     return str(x) == str(x)[::-1] 