"""
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Constraints:

* 3 <= s.length <= 5 x 10^4
* s only consists of a, b or c characters.
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        return -1


import pytest
target = Solution()

@pytest.mark.parametrize("txt, expect",
[
    ("abc", 1),
])
def test_numberOfSubstrings(txt, expect):
    assert target.numberOfSubstrings(txt) == expect