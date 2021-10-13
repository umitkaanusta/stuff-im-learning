"""
B. Fair Division
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output

Alice and Bob received n candies from their parents.
Each candy weighs either 1 gram or 2 grams. Now they want to divide all candies
among themselves fairly so that the total weight of Alice's candies is equal
to the total weight of Bob's candies.

Check if they can do that.

Note that candies are not allowed to be cut in half.

Input
The first line contains one integer t (1≤t≤104) — the number of test cases. Then t test cases follow.

The first line of each test case contains an integer n (1≤n≤100) — the number of
candies that Alice and Bob received.

The next line contains n integers a1,a2,…,an — the weights of the candies.
The weight of each candy is either 1 or 2.

It is guaranteed that the sum of n over all test cases does not exceed 105.

Output
For each test case, output on a separate line:

"YES", if all candies can be divided into two sets with the same weight;
"NO" otherwise.
You can output "YES" and "NO" in any case (for example, the strings yEs, yes,
Yes and YES will be recognized as positive).
"""


def fair_divisible(weights):
    if sum(weights) % 2 == 1:
        print("NO")
        return
    weights = sorted(weights)
    alice = 0
    bob = 0
    while weights:
        if weights[-1] == 1 and bob - alice > 1:
            alice += weights.pop()
            alice += weights.pop()
        else:
            alice += weights.pop()
        if weights:
            if weights[-1] == 1 and alice - bob > 1:
                bob += weights.pop()
                bob += weights.pop()
            else:
                bob += weights.pop()
    text = "YES" if alice == bob else "NO"
    print(text)


if __name__ == '__main__':
    num_tests = int(input())
    all_weights = []
    for _ in range(num_tests):
        candles = int(input())
        weights_ = input().split(" ")
        weights_ = [int(w) for w in weights_]
        all_weights.append(weights_)
    for w in all_weights:
        fair_divisible(w)
    """fair_divisible([1, 1])
    fair_divisible([1, 2])
    fair_divisible([1, 2, 1, 2])
    fair_divisible([2, 2, 2])
    fair_divisible([2, 1, 2])
    fair_divisible([2, 1, 1, 1, 1])"""
