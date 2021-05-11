#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// reverse word if word size is >=5
//spinWords("Hey fellow warriors"),
// Equals("Hey wollef sroirraw"));

string spinWords(const string &str) {
    string spinned;
    int words = (int)count(str.begin(), str.end(), ' ') + 1;
    string wordArr[words];
    int wordPtr = 0;
    for (char c : str) {
        if (c == ' ') {
            wordPtr++;
            continue;
        }
        wordArr[wordPtr] += c;
    }
    for (string &word: wordArr) {
        if (word.size() >= 5) {
            reverse(word.begin(), word.end());
        }
        spinned += word + " ";
    }
    spinned.pop_back(); //pop the trailing space
    return spinned;
}

int main() {
    cout << (spinWords("Hey fellow warriors") == "Hey wollef sroirraw") << endl;
}
