// Recursive multiply
#include <bits/stdc++.h>
using namespace std;

int recursiveMultiply(int a, int b) {
    // cout << a << ":" << (a&1) << "x" << b << ":" << (b&1) <<"\n";
    if(a == 1) {
        return b;
    }
    if(b == 1) {
        return a;
    }
    if((a&1) == 0) {
        // Last bit 0 - divide by 2
        return recursiveMultiply(a >> 1, b) << 1;
    }
    if((b&1) == 0) {
        // Last bit 0 - divide by 2
        return recursiveMultiply(a, b >> 1) << 1;
    }
    return b + (recursiveMultiply(a >> 1, b) << 1); // b + (b*(a-1)/2)*2
}

int main() {
    int num1 = 0, num2 = 0;
    // Due to time constraints, this program does not validate non-integer inputs.
    while(num1 <= 0) {
        cout << "First Positive Integer: ";
        cin >> num1;
    }
    while(num2 <= 0) {
        cout << "Second Positive Integer: ";
        cin >> num2;
    }
    cout << "Product: " << recursiveMultiply(num1, num2) << "\n";
    return 0;
}