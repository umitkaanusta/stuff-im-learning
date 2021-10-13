"""
E. Array Game
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output

Alice and Bob are playing a game. They are given an array A of length N.
The array consists of integers. They are building a sequence together.
In the beginning, the sequence is empty.
In one turn a player can remove a number from the left or right side of the array
and append it to the sequence. The rule is that the sequence they are building must be strictly increasing.
The winner is the player that makes the last move. Alice is playing first.
Given the starting array, under the assumption that they both play optimally, who wins the game?

Input
The first line contains one integer N (1≤N≤2∗105) - the length of the array A.

The second line contains N integers A1, A2,...,AN (0≤Ai≤109)

Output
The first and only line of output consists of one string, the name of the winner.
If Alice won, print "Alice", otherwise, print "Bob".
"""

from collections import deque


def array_game(n, array):
    left = 0
    right = n - 1
    while left < n - 1 and array[left] < array[left + 1]:
        left += 1
    while right >= 0 and array[right] < array[right - 1]:
        right -= 1
    if left % 2 == 0 or (n - right) % 2 == 1:
        print("Alice")
    else:
        print("Bob")


if __name__ == '__main__':
    N = int(input())
    integers = input().split(" ")
    integers = [int(el) for el in integers]
    array_game(N, integers)
    # array_game(1, [5])
    # array_game(3, [5, 4, 5])
    # array_game(6, [5, 8, 2, 1, 10, 9])
