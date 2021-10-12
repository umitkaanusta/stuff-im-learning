"""

B. Fafa and the Gates
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output

Two neighboring kingdoms decided to build a wall between them with some gates to enable the citizens
to go from one kingdom to another. Each time a citizen passes through a gate, he has to pay one silver coin.

The world can be represented by the first quadrant of a plane and the wall is built along the identity line
(i.e. the line with the equation x = y). Any point below the wall belongs to the first kingdom while
any point above the wall belongs to the second kingdom.
There is a gate at any integer point on the line (i.e. at points (0, 0), (1, 1), (2, 2), ...).
The wall and the gates do not belong to any of the kingdoms.

Fafa is at the gate at position (0, 0) and he wants to walk around in the two kingdoms.
He knows the sequence S of moves he will do. This sequence is a string where each character represents a move.
The two possible moves Fafa will do are 'U' (move one step up, from (x, y) to (x, y + 1)) and
'R' (move one step right, from (x, y) to (x + 1, y)).

Fafa wants to know the number of silver coins he needs to pay to walk around the two kingdoms
following the sequence S. Note that if Fafa visits a gate without moving from one kingdom to another,
he pays no silver coins. Also assume that he doesn't pay at the gate at point (0, 0), i. e.
he is initially on the side he needs.

Input
The first line of the input contains single integer n (1 ≤ n ≤ 105) — the number of moves in the walking sequence.

The second line contains a string S of length n consisting of the characters
'U' and 'R' describing the required moves. Fafa will follow the sequence S in order from left to right.

Output
On a single line, print one integer representing the number of silver coins
Fafa needs to pay at the gates to follow the sequence S.
"""


def walk_gates(sequence: str):
    positions = [(0, 0)]
    pay = 0
    for move in sequence:
        if move == "U":
            positions.append((positions[-1][0], positions[-1][1] + 1))
        elif move == "R":
            positions.append((positions[-1][0] + 1, positions[-1][1]))
        if len(positions) >= 3:
            curr = positions[-1]
            prev = positions[-2]
            prevprev = positions[-3]
            # conditions showing transition to another kingdom
            cond1 = curr[0] > prev[0] > prevprev[0]
            cond2 = prevprev[0] > prev[0] > curr[0]
            cond3 = curr[1] > prev[1] > prevprev[1]
            cond4 = prevprev[1] > prev[1] > curr[1]
            if prev[0] == prev[1] and any([cond1, cond2, cond3, cond4]):
                pay += 1
    # return positions, pay
    print(pay)


if __name__ == '__main__':
    # print(walk_gates(["U", "R", "U", "R", "R", "U", "U"]))
    # ([(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4)], 2)
    n = input()
    seq = input()
    walk_gates(seq)
