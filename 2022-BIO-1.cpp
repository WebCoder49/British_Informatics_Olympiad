#include <bits/stdc++.h>
using namespace std;
int main() {
    // First - 17min
    string word;
    std::cin >> word;
    int wordSize = word.size();

    int letters [wordSize];

    // Replace w/ number
    for (int i = 0; i < wordSize; i++) {
        letters[i] = int(word[i]) - 64; // From 1
    }

    // Not first letter - decrypt backwards
    for (int i = wordSize-1; i > 0; i--) {
        letters[i] -= letters[i-1];
        // Handle out-of-range
        if(letters[i] < 1) {
            letters[i] += 26;
        }
    }

    // Replace w/ letter - could only save next letter
    for (int i = 0; i < wordSize; i++) {
        word[i] = char(letters[i] + 64); // From 1
    }
    
    for (int letter: letters) {
        std::cout << letter << " ";
    }
    std::cout << "\n";
    std::cout << word;
}