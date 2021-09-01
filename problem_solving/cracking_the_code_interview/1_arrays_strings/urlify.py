"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
"""

# additional question: will we replace two spaces with %20%20 or just with %20?
# additional question 2: will we put %20 at the spaces at the 0th index?


def urlify(string, str_length):
    # O(n) time, O(n) space
    space = "%20"
    urlified = []
    for i in range(str_length):
        if string[i] == " ":
            urlified.append(space)
        else:
            urlified.append(string[i])
    return "".join(urlified)


def urlify_inplace(string, str_length):
    # Assuming we have an array of chars, this is an inplace algo
    space = "%20"
    urlified = list(string)
    for i in range(str_length):
        if urlified[i] == " ":
            urlified[i] = space
    j = str_length
    while True:
        try:
            urlified[j] = ""
            j += 1
        except IndexError:
            break
    return "".join(urlified)


def test_solutions():
    print(urlify("Mr John Smith ", 13))
    print(urlify_inplace("Mr John Smith ", 13))
    assert urlify("Mr John Smith ", 13) == "Mr%20John%20Smith"
    assert urlify_inplace("Mr John Smith ", 13) == "Mr%20John%20Smith"


if __name__ == '__main__':
    test_solutions()
