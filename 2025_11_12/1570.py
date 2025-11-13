# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/
"""
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

* SparseVector(nums) Initializes the object with the vector nums
* dotProduct(vec) Compute the dot product between the instance of SparseVector and vec

A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?
"""

class SparseVector:
    def __init__(self, nums):
        self.dict = {}
        for i, n in enumerate(nums):
            if n is not 0:           
                self.dict[i] = n
        self.length = len(self.dict)
        return

    def dotProduct(self, vec : SparseVector) -> int:
        
        a, b = self.dict, vec.dict if self.length < vec.length else vec.dict, self.dict

        res = 0
        for i, n in a.items():

            if i in b.dict:
                res += n * b.dict[i]
        
        return res








vec1 = SparseVector()
vec2 = SparseVector()

vec1.dotProduct(vec2)