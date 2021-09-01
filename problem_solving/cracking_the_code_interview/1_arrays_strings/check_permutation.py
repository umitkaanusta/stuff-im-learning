"""
Given two strings, write a method to decide if one is a permutation of the
other.
"""


def check_str_permutation(s1, s2):
    # logic: if both strings have the same characters with same frequencies, they're perms.
    # we'll use a hash table, but collections.Counter is a more elegant but less interview-y solution
    # Time: O(n), Space: O(2*n) = O(n)
    if len(s1) != len(s2):
        return False  # no need to check strings of different length
    ht1 = {}
    ht2 = {}
    for c in s1:
        ht1[c] = 1 if c not in ht1 else ht1[c] + 1
    for c in s2:
        ht2[c] = 1 if c not in ht2 else ht2[c] + 1
    for c in ht1:
        if c not in ht2 or ht2[c] != ht1[c]:
            return False
    return True


# another solution might be sorting the strings and checking s1 == s2


def test_solutions():
    assert check_str_permutation("mercedes", "dermeces")
    assert not check_str_permutation("cat", "dog")


if __name__ == '__main__':
    test_solutions()
