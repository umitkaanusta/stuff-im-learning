#include <iostream>
using namespace std;

// Coin-collecting problem
// NxM board: 0 means no coins, 1 means there's a coin there
// robot starts in top-left corner
// ends in bottom-right corner
// Collect as many coins as possible
// Allowed moves: one step right, one step down (only one of them at each turn)


int collect(int rows, int cols, int** board) {
    // DP approach
    int output[rows][cols];
    output[0][0] = board[0][0];
    for (int j = 1; j < cols; j++) {
        output[0][j] = output[0][j - 1] + board[0][j];
    }
    for (int i = 1; i < rows; i++) {
        output[i][0] = output[i - 1][0] + board[i][0];
        for (int j = 1; j < cols; j++) {
            output[i][j] = board[i][j] +
                    max(output[i - 1][j], output[i][j - 1]);
        }
    }
    return output[rows - 1][cols - 1];
}

int main() {
    int rows = 5;
    int cols = 6;
    int **board = (int**)malloc(rows * sizeof(int*));
    for (int i = 0; i < rows; i++)
        board[i] = (int*)malloc(cols * sizeof(int));
    board[0][4] = 1;
    board[1][1] = 1;
    board[1][3] = 1;
    board[2][3] = 1;
    board[2][5] = 1;
    board[3][2] = 1;
    board[3][5] = 1;
    board[4][0] = 1;
    board[4][4] = 1;
    cout << (collect(rows, cols, board) == 5) << endl;
    return 0;
}
