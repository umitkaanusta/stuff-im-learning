"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""


def is_max_one_edit_away(s1, s2):
    # O(n)
    # case 0: if strings are equal they're 0 edits away
    if s1 == s2:
        return True
    # case 1: if len(s1) == len(s2), only one character should be replaced
    if len(s1) == len(s2):
        num_nonmatching_chars = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                num_nonmatching_chars += 1
        if num_nonmatching_chars <= 1:
            return True
    # case 2: if abs(len(s1) - len(s2)) == 1, only one character should be added/removed
    # there should be only one different char
    elif abs(len(s1) - len(s2)) == 1:
        i = 0
        j = 0
        num_nonmatching_chars = 0
        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                num_nonmatching_chars += 1
                if len(s1) > len(s2):
                    i += 1
                    continue
                elif len(s1) < len(s2):
                    j += 1
                    continue
            i += 1
            j += 1
        if num_nonmatching_chars <= 1:
            return True
    return False


def test_solution():
    assert is_max_one_edit_away("pale", "ple")
    assert is_max_one_edit_away("pales", "pale")
    assert is_max_one_edit_away("pale", "bale")
    assert not is_max_one_edit_away("pale", "bake")


if __name__ == '__main__':
    test_solution()
