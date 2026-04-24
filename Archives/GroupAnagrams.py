# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict # Import defaultdict to automatically handle missing keys

class Solution(object):
    def groupAnagrams(self, strs):
        # Hash Table
        res = defaultdict(list) # Create a dictionary where each new key has a default empty list
        for s in strs:
            count = [0]*26 # a...z
            for c in s:
                count[ord(c)-ord('a')]+=1 # ascii code -> (ord)
                # Convert count list to a tuple to use it as a key (lists can't be dictionary keys)
            res[tuple(count)].append(s) # Group the word under its character count signature
            
        return list(res.values())
        

    # HashMap : key => identify the anagrams (Number of occurrences of the letter in the word , letter)
    # value => list of anagrams
    # 1e 1a 1t (key) => [eat,ate,tea] (value)
    # O(m.n) : m : total number of inputs given | n : avg length of a string
    
        
        
