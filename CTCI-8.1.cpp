// Triple Step
#include <bits/stdc++.h>
using namespace std;

class Counter {
    private:
        map<int,int> waysForSteps; // numSteps ==> numWays (memoisation)
    public:
        int countWays(int numSteps) {
            if(waysForSteps.count(numSteps) == 1) return waysForSteps[numSteps];

            if(numSteps < 0) return 0; // So 1 step gives 1
            if(numSteps == 0) return 1;

            int numWays = countWays(numSteps-1)
                    + countWays(numSteps-2)
                    + countWays(numSteps-3);

            waysForSteps[numSteps] = numWays;
            return numWays;
        }
};

int recursive() {
    int numSteps;
    Counter counter;

    cin >> numSteps;
    cout << counter.countWays(numSteps) << "\n";

    return 0;
}

int iterative() {
    // TODO
    int numSteps;

    cin >> numSteps;

    int numWays = 1;
    int numWays1StepBefore = 0;
    int numWays2StepsBefore = 0;
    int numWays3StepsBefore = 0;

    for(int i = 0; i < numSteps; i++) {
        numWays3StepsBefore = numWays2StepsBefore;
        numWays2StepsBefore = numWays1StepBefore;
        numWays1StepBefore = numWays;
        numWays = numWays1StepBefore + numWays2StepsBefore + numWays3StepsBefore;
    }

    cout << numWays;

    return 0;
}

int main() {
    recursive();
    return iterative();
}