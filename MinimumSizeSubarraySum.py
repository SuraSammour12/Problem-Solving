# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution(object):
    def minSubArrayLen(self, target, nums):
        # Sliding Window : Variable Window  
        left = 0 # left boundary of the sliding window
        total = 0 # current sum inside the window
        min_len = float('inf') # infinity : minimum length 
        for right in range(len(nums)): # expand window from the right 
            total+=nums[right] # add current number to the total
            while total>=target:
                min_len = min(min_len,right-left+1)
                total-=nums[left] # shrink the window from the left
                left+=1
        # ternary operator
        return 0 if min_len==float('inf') else min_len
       
                                 



        