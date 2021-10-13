"""
B. Draw!
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output

You still have partial information about the score during the historic football match.
You are given a set of pairs (ai,bi), indicating that at some point during the match the
score was "ai: bi". It is known that if the current score is «x:y»,
then after the goal it will change to "x+1:y" or "x:y+1".
What is the largest number of times a draw could appear on the scoreboard?

The pairs "ai:bi" are given in chronological order (time increases),
but you are given score only for some moments of time. The last pair corresponds to the end of the match.

Input
The first line contains a single integer n (1≤n≤10000) — the number of known moments in the match.

Each of the next n lines contains integers ai and bi (0≤ai,bi≤109),
denoting the score of the match at that moment (that is, the number of goals
by the first team and the number of goals by the second team).

All moments are given in chronological order, that is, sequences xi and yj are non-decreasing.
The last score denotes the final result of the match.

Output
Print the maximum number of moments of time, during which the score was a draw.
The starting moment of the match (with a score 0:0) is also counted.
"""


def max_num_of_draws(scores):
    x = 0
    y = 0
    draws = 1
    for score_x, score_y in scores:
        draws += max(0, min(score_x, score_y) - max(x, y) + int(x != y))
        x, y = score_x, score_y
    print(draws)
    return draws


if __name__ == '__main__':
    n = int(input())
    score_inputs = []
    for _ in range(n):
        score_inputs.append(tuple(input().split(" ")))
    score_inputs = [(int(x), int(y)) for x, y in score_inputs]
    max_num_of_draws(score_inputs)
    """assert max_num_of_draws([(0, 0), (2, 2), (6, 5), (7, 7)]) == 8
    assert max_num_of_draws([(2, 0), (3, 1), (3, 4)]) == 2
    assert max_num_of_draws([(0, 0), (0, 0), (0, 0)]) == 1
    assert max_num_of_draws([(5, 4)]) == 5
    assert max_num_of_draws([(5, 5)]) == 6"""
