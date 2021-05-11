#include <map>
#include <string>
#include <iostream>
using namespace std;

// convert roman to int
// Symbol    Value
// I          1
// V          5
// X          10
// L          50
// C          100
// D          500
// M          1,000

int solution(const string &roman) {
    map<char, int> symbols = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
                              {'C', 100}, {'D', 500}, {'M', 1000}};
    int soln = 0;
    for (int i = 0; i < roman.size() - 1; i++) {
        int value = symbols[roman[i]];
        if (value < symbols[roman[i + 1]]) {
            value = -value;
        }
        soln += value;
    }
    return soln + symbols[roman[roman.size() - 1]];
}


int main() {
    cout << (solution("CLXXXII") == 182) << endl;
    cout << (solution("MCMXC") == 1990) << endl;

    return 0;
}
