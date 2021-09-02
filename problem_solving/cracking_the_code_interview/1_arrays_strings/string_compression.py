"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""


def compress_string(string):
    # O(n)
    last_seen_char = None
    local_freq = 0  # local frequency, frequency of a char in a continuous sequence containing only that char
    compressed = []
    for i in range(len(string)):
        if string[i] != last_seen_char:
            # if current char is different than the last seen one
            if i != 0:
                compressed.append(str(local_freq))  # append previous char's count
            compressed.append(string[i])  # append the curr char
            if i == len(string) - 1:
                # if we're at the last char, and that char is different from
                # the previous one, append "1" at the end to denote its "local frequency"
                compressed.append("1")
            last_seen_char = string[i]
            local_freq = 1  # set its count to 1
        elif i == len(string) - 1 and string[i] == last_seen_char:
            compressed.append(str(local_freq + 1))
        else:
            local_freq += 1
    compressed = "".join(compressed)
    if len(compressed) < len(string):
        return compressed
    return string


def test_solution():
    """aabcccccaaa would become a2b1c5a3."""
    assert compress_string("aabcccccaaa") == "a2b1c5a3"
    assert compress_string("aabcccccaad") == "a2b1c5a2d1"
    assert compress_string("aaaaaaaaaaa") == "a11"
    assert compress_string("abcde") == "abcde"


if __name__ == "__main__":
    test_solution()
