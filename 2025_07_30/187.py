# https://leetcode.com/problems/repeated-dna-sequences/description/
"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
* For example, "ACGAATTCCG" is a DNA sequence.

When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
You may return the answer in any order.


Constraints:

* 1 <= s.length <= 10^5
* s[i] is either 'A', 'C', 'G', or 'T'.


Example:
* Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
* Output: ["AAAAACCCCC","CCCCCAAAAA"]


# 1, set = ("AAAAACCCCC", "AAAACCCCCA")
# 2, 

"""
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        read = set()
        res = set()
        
        for i in range(10, len(s)+1):
            curr = s[i-10:i]
            if curr in read:
                res.add(curr) # if read, then appearred twice, add as output
            else:
                read.add(curr)
            
        return [r for r in res]
