# Minimal change, decrease-by-1 algorithm
# Given n, calculate all permutations of [1, 2, ..., n]

# I designed this algo on paper using pseudocode with a time constraint, more efficient versions of it can of course be designed
# Using bottom-up approach

from math import factorial

def perms(n):
    perms = ["1"]
    if n == 1:
        return perms
    start = 0
    end = 1
    for i in range(2, n + 1):
        for k in range(start, end):
            for idx in range(0, len(perms[k]) + 1):
                perms.append(insert_str(perms[k], idx, i))
        start += factorial(i - 1)
        end += factorial(i)
    return perms[start:]
    
def insert_str(string, idx, val):
    return string[:idx] + str(val) + string[idx:]
    
if __name__ == "__main__":
    assert sorted(perms(2)) == ["12", "21"]
    assert sorted(perms(3)) == ["123", "132", "213", "231", "312", "321"]
