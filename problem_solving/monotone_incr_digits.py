class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10:
            return n
        break_point = None
        digits = [int(el) for el in str(n)]
        for i in range(len(digits) - 1):
            if digits[i] > digits[i + 1]:
                break_point = i
                break
        if break_point is None:
            return n
        # if break point is in a consecutive series of numbers, move it to the
        # index of first element of the abovesaid series of numbers
        while i > 0 and digits[i] == digits[i - 1]:
            break_point -= 1
            i -= 1
        digits[break_point] -= 1
        digits[break_point + 1:] = [9] * (len(digits) - break_point - 1)
        return int("".join(map(str, digits)))
        
