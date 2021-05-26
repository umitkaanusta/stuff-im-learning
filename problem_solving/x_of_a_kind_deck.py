from collections import Counter
from math import gcd
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        c = Counter(deck)
        gcd_ = reduce(gcd, c.values())
        if gcd_ == 1:
            return False
        for val in c.values():
            if val < 2:
                return False
        return True
