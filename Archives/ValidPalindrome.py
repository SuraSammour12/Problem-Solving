# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/


"""
First solution
class Solution(object):
    def isPalindrome(self, s):
        clean=""
        for c in s:
            if ('a'<=c<='z') or ('A'<=c<='Z') or ('0'<=c<='9'):
                clean += c.lower()
        return clean == clean[::-1]
"""
           
# The Second solution
class Solution(object):
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1  # Initialize two pointers

        while left < right:
            # Skip non-alphanumeric from the left side
            while left < right and not s[left].isalnum():# isalnum() is a built-in function in Python, used to check if a character is a letter or a number
                left += 1

            # Skip non-alphanumeric from the right side
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare lowercase letters
            if s[left].lower() != s[right].lower():
                return False  # not a palindrome

            left += 1  # Move both pointers inward
            right -= 1

        return True  # All checks passed, it's a palindrome

        
