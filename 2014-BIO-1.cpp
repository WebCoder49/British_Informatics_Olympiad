// Lucky Numbers

#include <bits/stdc++.h>
using namespace std;

// 2023-11-11 Marking (1 right, 0 wrong, * bug):
// 11111111 25/25, b:2/2
// Took 00h41m32s

class LuckyGenerator {
        vector<int> rotationPeriods;
        vector<int> remaindersRotating;
    public:
        void answerFor(int max) {
            
            int latestLuckyNumber = 1;
            int listIndex = 1;

            for(int currentOddNumber = 3; true; currentOddNumber += 2) {

                if(currentOddNumber == max || currentOddNumber == max+1) {
                    cout << latestLuckyNumber << " "; // Closest less than input
                }

                bool luckyNumber = true;
                for(int i = 0; i < rotationPeriods.size(); i++) {
                    remaindersRotating[i] += 1;
                    if(remaindersRotating[i] == rotationPeriods[i]) {
                        // So "rotates"
                        remaindersRotating[i] = 0;
                        
                        luckyNumber = false;
                        break; // This isn't lucky - has been taken out; don't rotate larger nums as this was removed before larger nums processed
                    }
                }
                if(luckyNumber) {
                    // Lucky number found
                    if(currentOddNumber > max) {
                        cout << currentOddNumber << "\n"; // Closest greater than input
                        return;
                    }
                    latestLuckyNumber = currentOddNumber;

                    rotationPeriods.push_back(currentOddNumber);
                    remaindersRotating.push_back((listIndex+1) % currentOddNumber);
                    listIndex++;
                }
            }
        }
};

int main() {
    LuckyGenerator luckyGenerator;
    int n;
    cin >> n;
    luckyGenerator.answerFor(n);
}