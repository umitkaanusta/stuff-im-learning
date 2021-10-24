from collections import Counter, defaultdict

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # if all characters in the string appear in the string allowed.
        allowed_chars = defaultdict(bool)
        consistent = 0
        for char in allowed:
            allowed_chars[char] = True
        for word in words:
            word_consistent = True
            for char in word:
                if not allowed_chars[char]:
                    word_consistent = False
                    break
            consistent += int(word_consistent)
        return consistent
