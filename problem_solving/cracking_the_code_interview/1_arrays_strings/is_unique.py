"""
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""


def is_str_unique(string):
    # brute force, O^2, no additional data structures
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True


def is_str_unique_HT(string):
    # O(n) solution using a hash table
    exists = {}
    for c in string:
        if c not in exists:
            exists[c] = True
        else:
            return False
    return True

# sorting the input string is described as another no-additional-data-structures solution in the book
# but python doesn't allow that


def test_solution():
    assert not is_str_unique("avavavava")
    assert is_str_unique("trying")

    assert not is_str_unique_HT("avavavava")
    assert is_str_unique_HT("trying")


if __name__ == '__main__':
    test_solution()
