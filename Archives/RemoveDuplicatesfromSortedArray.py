# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        # Two Pointers
        if not nums: # Empty list
            return 0
        i = 0 # this pointer for the last unique number, i start from the 1st number
        for j in range(1,len(nums)):
            if nums[j] != nums[i]: # find a unique number nums[j]
               i+=1 # new place for the new unique num
               nums[i]=nums[j]
        return i+1 # number of unique elements; i is index-based (starts from 0), count starts from 1
        
        
