"""
Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.

[1 2 4 5 6] + 3 = [1 2 4 5 6 3] -> [1 2 4 5 3 6] -> [1 2 4 3 5 6] -> [1 2 3 4 5 6]
                             l              l              l              l
"""


class SortedStack:
    def __init__(self):
        self.data = []

    def __str__(self):
        return str(self.data)

    def push(self, el):
        # insertion sort
        self.data.append(el)
        j = len(self.data) - 2
        while j >= 0 and el < self.data[j]:
            self.data[j + 1] = self.data[j]
            j -= 1
        self.data[j + 1] = el

    def pop(self):
        if not self.is_empty():
            return self.data.pop()

    def peek(self):
        return self.data[-1] if not self.is_empty() else None

    def is_empty(self):
        return bool(self.data)


def test_solution():
    st = SortedStack()
    st.push(3)
    st.push(6)
    assert st.data == [3, 6]
    st.push(1)
    assert st.data == [1, 3, 6]
    st.push(4)
    assert st.data == [1, 3, 4, 6]
    st.push(5)
    assert st.data == [1, 3, 4, 5, 6]
    st.push(2)
    assert st.data == [1, 2, 3, 4, 5, 6]


if __name__ == '__main__':
    test_solution()
