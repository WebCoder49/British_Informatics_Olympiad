#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1) {
            // Read as normal
            return s;
        }

        int downupLength = ((2*numRows)-2);
        int stringLength = s.length();
        int numDownups = stringLength / downupLength;// Number of complete zig-downs and zag-ups; int div as div of ints
        int finaldownupLength = stringLength % downupLength;

        int rowIndices [numRows]; // zeroes

        // Generate row start indices
        // Ends only have 1 letter per downup
        rowIndices[0] = 0;
        rowIndices[1] = numDownups;
        // Partially-completed downup - never part of "up"
        if(0 < finaldownupLength) {
            // First down part of downup
            rowIndices[1] += 1;
        }

        // cout << "numDownups: " << numDownups << "\n";

        for(int i = 2; i < numRows; i++) {
            // Other rows have 2 letters per downup
            rowIndices[i] = rowIndices[i-1] + (numDownups*2);

            // Partially-completed downup
            if(i-1 > downupLength-finaldownupLength) {
                // Second up part of downup
                rowIndices[i] += 2;
            } else if(i-1 < finaldownupLength) {
                // First down part of downup
                rowIndices[i] += 1;
            }
        }
        // // cout << "[";
        // for(int index : rowIndices) {
        //     cout << index << " ";
        // }
        // cout << "]\n";

        // Add letters to rows
        char outputChars [stringLength+1];
        int rowI = 0;
        bool directionReversed = false;
        for (char chr : s) {
            // Add to row by rowI
            outputChars[rowIndices[rowI]] = chr;
            rowIndices[rowI] = rowIndices[rowI] + 1; // Increment

            if(directionReversed) {
                if(rowI == 0) {
                    directionReversed = false;
                    rowI++;
                } else {
                    rowI--;
                }
            } else {
                if(rowI == numRows-1) {
                    directionReversed = true;
                    rowI--;
                } else {
                    rowI++;
                }
            }
        }

        outputChars[stringLength] = '\0';

        string outputString = outputChars;
        
        return outputString; // TODO: Convert
    }
};