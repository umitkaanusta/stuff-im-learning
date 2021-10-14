"""
A. Football
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output

One day Vasya decided to have a look at the results of Berland 1910 Football Championship’s finals.
Unfortunately he didn't find the overall score of the match; however, he got hold
of a profound description of the match's process. On the whole there are n lines
in that description each of which described one goal. Every goal was marked with
the name of the team that had scored it. Help Vasya, learn the name of the team that won
the finals. It is guaranteed that the match did not end in a tie.

Input
The first line contains an integer n (1 ≤ n ≤ 100) — the number of lines in the description.
Then follow n lines — for each goal the names of the teams that scored it.
The names are non-empty lines consisting of uppercase Latin letters
whose lengths do not exceed 10 symbols. It is guaranteed that the match did not end in
a tie and the description contains no more than two different teams.

Output
Print the name of the winning team. We remind you that in football the team that scores
more goals is considered the winner.
"""


def get_winner(goals):
    score = {}
    for goal in goals:
        if goal not in score:
            score[goal] = 1
        else:
            score[goal] += 1
    teams = [*score.keys()]
    if len(teams) == 1:
        print(teams[0])
    else:
        print(teams[0] if score[teams[0]] > score[teams[1]] else teams[1])


if __name__ == '__main__':
    num_goals = int(input())
    goals_ = []
    for _ in range(num_goals):
        goals_.append(input())
    get_winner(goals_)
