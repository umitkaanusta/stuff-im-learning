"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
"""


class MinStack:
    def __init__(self):
        # implement using array
        # python lists have push, pop, peek etc.
        self.data = []
        self.mins = []
        self.min_so_far = 9999999

    def push(self, el):
        self.data.append(el)
        if el < self.min_so_far and el not in self.mins:
            self.mins.append(el)
            self.min_so_far = el

    def pop(self):
        popped = self.data.pop()
        if popped == self.min_so_far:
            self.mins.pop()
            self.min_so_far = self.mins[-1] if self.mins else 9999999
        return popped

    def min(self):
        return self.min_so_far

    def __str__(self):
        return str(self.data)


def test_solution():
    st = MinStack()
    st.push(999)
    assert st.min() == 999
    st.push(6)
    assert st.min() == 6
    st.push(5)
    assert st.min() == 5
    st.push(99)
    assert st.min() == 5
    st.push(99)
    assert st.min() == 5
    st.pop()
    st.pop()
    st.pop()
    assert st.min() == 6


if __name__ == '__main__':
    test_solution()
