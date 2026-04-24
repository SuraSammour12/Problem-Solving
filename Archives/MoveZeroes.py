# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        non_zero_index = 0 # pounter of a non-zero number

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        
        # after the last non-zero number, fill in zeros
        for i in range(non_zero_index,len(nums)):
            nums[i]=0
        
        
