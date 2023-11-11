// Down Pat
#include <bits/stdc++.h>
using namespace std;

// 2023-11-11 Marking (1 right, 0 wrong, * bug):
// 11111111111 24/24

bool splitPatReversed(int pat[], int start, int end);

/**
 * Return if the pat is valid (the pat is the subarray from `start` to `end`, `start < end`)
*/
bool splitPat(int pat[], int start, int end) {
    if(start >= end-1) {
        // cout << "Valid " << start << "\n";
        return true;
    }
    // cout << "Testing " << start << " " << end << "\n";

    // Find splits that follow left all greater than right rule
    // Try for each split index (index of rightmost char of left side)
    int leftMin = 26; // As alphabet 0 to 25
    for(int splitI = start; splitI < end-1; splitI++) {
        if(pat[splitI] < leftMin) { // TODO: Debug why split 3
            leftMin = pat[splitI];
        }

        // must follow left all greater than right rule
        bool valid = true;
        for(int checkRightI = splitI+1; checkRightI < end; checkRightI++) {
            if(pat[checkRightI] >= leftMin) {
                // cout << "Wrong" << checkRightI << "min" << leftMin << "\n";
                valid = false;
                break;
            }
        }
        if(valid) {
            // Valid pat at this split
            // cout << "Deeper " << start << " " << end << " Split@" << splitI+1 << "\n";
            if (splitPatReversed(pat, splitI+1, start) && splitPatReversed(pat, end, splitI+1)) {
                return true;
            }
        }
    }
    // cout << "Invalid " << start << " " << end << "\n";
    return false;
}

/**
 * Return if the pat is valid (the pat is the *reversed* subarray from `start` to `end`, `start > end`)
*/
bool splitPatReversed(int pat[], int start, int end) {
    if(start <= end+1) {
        // cout << "Valid " << start << "\n";
        return true;
    }
    // cout << "Testing Reversed " << start << " " << end << "\n";

    // Find splits that follow left all greater than right rule
    // Try for each split index (index of rightmost char of left side)
    int leftMin = 26; // As alphabet 0 to 25
    for(int splitI = start-1; splitI > end; splitI--) {
        if(pat[splitI] < leftMin) {
            leftMin = pat[splitI];
        }

        // must follow left all greater than right rule
        bool valid = true;
        for(int checkRightI = splitI-1; checkRightI >= end; checkRightI--) {
            if(pat[checkRightI] >= leftMin) {
                // cout << "Wrong" << checkRightI << "min" << leftMin << "\n";
                valid = false;
                break;
            }
        }
        if(valid) {
            // Valid pat at this split
            // cout << "Deeper Reversed " << start << " " << end << " Split@" << splitI << "\n";
            if (splitPat(pat, splitI, start) && splitPat(pat, end, splitI)) {
                return true;
            }
        }
    }
    // cout << "Invalid Reversed " << start << " " << end << "\n";
    return false;
}

string bool2YesNo(bool b) {
    return b ? "YES" : "NO";
}

int main() {
    string s1_str, s2_str;
    cin >> s1_str >> s2_str;

    int s1_len = s1_str.size();
    int s2_len = s2_str.size();

    int s1PlusS2[s1_len + s2_len]; // Concatenated

    for(int i = 0; i < s1_len; i++) {
        s1PlusS2[i] = s1_str[i] - 'A'; // A0,B1,C2...
        // cout << s1_str[i] - 'A' << "!";
    }
    for(int i = 0; i < s2_len; i++) {
        s1PlusS2[s1_len+i] = s2_str[i] - 'A'; // A0,B1,C2...
        // cout << s2_str[i] - 'A' << "!";
    }

    cout << bool2YesNo(splitPat(s1PlusS2, 0, s1_len)) << "\n";
    cout << bool2YesNo(splitPat(s1PlusS2, s1_len, s1_len+s2_len)) << "\n";
    cout << bool2YesNo(splitPat(s1PlusS2, 0, s1_len+s2_len)) << "\n";

    return 0;
}