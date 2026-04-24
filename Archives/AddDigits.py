# 258. Add Digits
# https://leetcode.com/problems/add-digits/

class Solution(object):
    def addDigits(self, num):
        while num >=10:
            total = 0
            for digit in str(num):
                total += int(digit)
            num = total
        return num

      
