class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        colors = list(colors)
        which_color = {True: "A", False: "B"}
        satisfying = {True: 0, False: 0}
        if len(colors) < 3:
            return False
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1] == which_color[True]:
                satisfying[True] += 1
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1] == which_color[False]:
                satisfying[False] += 1
        return satisfying[True] > satisfying[False]
