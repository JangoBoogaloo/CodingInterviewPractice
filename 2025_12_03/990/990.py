"""
You are given an array of strings equations that represent relationships between variables
where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".
Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.


"a!=a"

"a==b", "b==c", "a!=c"

Example 1:

Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.


Example 2:

Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

# if check all ==, true  => set(a, b, c, d, e ...)

# if check all !=,  x != y, true, x!= x false

Constraints:

* 1 <= equations.length <= 500
* equations[i].length == 4
* equations[i][0] is a lowercase letter.
* equations[i][1] is either '=' or '!'.
* equations[i][2] is '='.
* equations[i][3] is a lowercase letter.
"""
from typing import List
from collections import Counter, defaultdict

"""
a==b true
a!=a false
a==b, b!=a false
a!=b, b!=c true

"""

class Solution:

    def equationsPossible(self, equations: List[str]) -> bool:
        
        uf = UF()
        
        # filter out equals
        equals = filter(equations, lambda x: x[1] == "=")
        non_equals = filter(equations, lambda x: x[1] == "!")

        for x, _, _, y in equals:
            uf.add(x)
            uf.add(y)
            uf.union(x, y)
        
        for x, _, _, y in non_equals:
            if not uf.valid(x) or not uf.valid(y):
                continue
            if x == y or uf.find(x) == uf.find(y):
                return False
        return True
    

class UF:
    def __init__(self):
        self._rank = Counter()
        self._parent = defaultdict()
        self._count = 0
        return

    def add(self, data) -> None:
        if self._parent.get(data) is None:
            self._parent[data] = data
            self._count += 1

    def valid(self, data) -> bool:
        return self._parent.get(data) is not None

    def find(self, data):
        if self._parent.get(data) is None:
            raise ValueError(f"data {data} is not added")
        if self._parent.get(data) != data:
            self._parent[data] = self.find(self._parent.get(data))
        return self._parent[data]

    def union(self, data1, data2) -> None:
        data1Root, data2Root = self.find(data1), self.find(data2)
        if data1Root == data2Root:
            return
        if self._rank[data1Root] > self._rank[data2Root]:
            self._parent[data2Root] = data1Root
        elif self._rank[data1Root] < self._rank[data2Root]:
            self._parent[data1Root] = data2Root
        else:
            self._parent[data2Root] = data1Root
            self._rank[data1Root] += 1
        self._count -= 1

    def __len__(self):
        return self._count