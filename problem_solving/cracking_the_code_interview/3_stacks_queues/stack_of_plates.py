"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).

FOLLOW UP
Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.
"""
from typing import List


class Stack:
    def __init__(self):
        self.data = []
        self.capacity = 5

    def push(self, el):
        if len(self.data) < self.capacity:
            self.data.append(el)
        else:
            return False

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return False

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class SetOfStacks:
    def __init__(self, stacks=None):
        # list of "Stack"s
        self.stacks: List[Stack] = stacks if stacks is not None else []

    def create_new_stack(self):
        self.stacks.append(Stack())

    def get_convenient_stack_idx_push(self):
        convenient_idx = None
        for i, st in enumerate(self.stacks):
            if len(st.data) < st.capacity:
                convenient_idx = i
                break
        if convenient_idx is None:
            self.create_new_stack()
            convenient_idx = len(self.stacks) - 1
        return convenient_idx

    def get_convenient_stack_idx_pop(self):
        convenient_idx = None
        for i in range(len(self.stacks) - 1, -1, -1):
            if len(self.stacks[i].data) > 0:
                convenient_idx = i
                break
        return convenient_idx

    def push(self, el):
        stack_idx = self.get_convenient_stack_idx_push()
        self.stacks[stack_idx].push(el)

    def pop(self):
        pop_idx = self.get_convenient_stack_idx_pop()
        if pop_idx is not None:
            return self.stacks[pop_idx].pop()
        return False

    def pop_at(self, idx):
        return self.stacks[idx].pop()

    def __str__(self):
        return str(self.stacks)

    def __getitem__(self, item):
        return self.stacks[item]


def test_solution():
    case = SetOfStacks([Stack()])
    case.push(3)
    assert case[0].data == [3]
    case.push(3)
    case.push(3)
    case.push(3)
    case.push(3)
    case.push(3)
    assert case[0].data == [3, 3, 3, 3, 3] and case[1].data == [3]
    case.pop()
    assert case[1].data == []
    case.push(5)
    case.pop_at(0)
    assert case[0].data == [3, 3, 3, 3] and case[1].data == [5]


if __name__ == '__main__':
    test_solution()
