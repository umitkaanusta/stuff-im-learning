"""
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""


def is_palindrome_permutation(string):
    # example says no need to look at case sensitivity and spaces
    # there could be 2 types of palindromes:
    # number 1 - aaccaa, all characters occur even number of times
    # number 2 - aacbbbcaa, one character occur at odd number of times the others occur even number of times
    # O(n) solution
    string = string.lower().replace(" ", "")
    odd = {}
    for c in string:
        odd[c] = True if c not in odd else not odd[c]
    # if more than 1 character occur odd number of times, it's over.
    num_chars_occuring_odd_number_of_times = 0
    for c in odd:
        if odd[c]:
            num_chars_occuring_odd_number_of_times += 1
        if num_chars_occuring_odd_number_of_times > 1:
            return False
    return True


def is_palindrome_permutation_bitvector(string):
    # another approach discussed in the book
    # idea: no need to know the number of occurrences of each char
    # also no need to know which chars occur odd/even number of times
    # we just need to assure that at most one char occurs odd number of times
    #
    # assume english alphabet, this may dramatically increase space complexity if
    # the set of values are not limited to the english alphabet
    #
    # at most one bit should be 1
    # So, we can check to see that a number has exactly one 1 because if we subtract 1
    # from it and then AND it with the new number, we should get 0.
    # 00010000 - 1 = 00001111
    # 00010000 & 00001111 = 0
    # O(n)
    string = string.lower().replace(" ", "")
    odd = 0  # our bit vector
    for c in string:
        char_idx = ord(c) - 97
        mask = 1 << char_idx
        odd = (odd | mask) if (odd & mask) else (odd & mask)
    return odd == 0 or (odd & (odd - 1)) == 0


def test_solutions():
    assert is_palindrome_permutation("Tact Coa")
    assert is_palindrome_permutation_bitvector("Tact Coa")


if __name__ == '__main__':
    test_solutions()
