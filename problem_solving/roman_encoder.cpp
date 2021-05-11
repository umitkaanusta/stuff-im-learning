#include <map>
#include <string>
#include <iostream>
using namespace std;

// convert int to roman
// Symbol    Value
// I          1
// V          5
// X          10
// L          50
// C          100
// D          500
// M          1,000

string solution(int number) {
    int values[13] = {1000, 900, 500, 400, 100, 90, 50,
                      40, 10, 9, 5, 4, 1};
    string symbols[13] = {"M", "CM", "D", "CD", "C", "XC", "L",
                          "XL", "X", "IX", "V", "IV", "I"};
    int i = 0;
    string roman;
    while (number > 0) {
        if (values[i] <= number) {
            number -= values[i];
            roman += symbols[i];
        }
        else {
            i++;
        }
    }
    return roman;
}


int main() {
    cout << (solution(182) == "CLXXXII") << endl;
    cout << (solution(1990) == "MCMXC") << endl;

    return 0;
}
