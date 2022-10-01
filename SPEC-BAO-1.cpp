#include <bits/stdc++.h>
using namespace std;


int alphabetI(char uppercaseLetter) {
    return int(uppercaseLetter) - 65; // ASCII
}

int main() {
  cout << "Hello World!\n";

  string chrs;
  cin >> chrs;

  // Initialise vars
  int lenChrs = chrs.length();
  set<string> visitedWords;

  bool hasPortals = true;
  while (hasPortals) {
    hasPortals = false;
    // Check not infinite loop
    if(visitedWords.count(chrs)!=0) {
      hasPortals = true;
      cout << "Indefinite\n";
      break;
    }
    visitedWords.insert(chrs);
    // Look for first portal and "teleport" it
    for (int i = 0; i < lenChrs-1; i++) {
      int firstLetterI = alphabetI(chrs[i]);
      int secondLetterI = alphabetI(chrs[i+1]);
      // cout << firstLetterI << " " << secondLetterI << "\n";
      if(firstLetterI == 25-secondLetterI) {
        // Portal
        // Letter `i`s now around "portal" first letter

        if(secondLetterI > firstLetterI) {
          // Move surrounding chrs to end
          if(i != 0) {
            chrs.append(string(1,chrs[i-1]));
          }
          chrs.append(string(1,chrs[i+1]));
          chrs.erase(i+1, 1);
          if(i != 0) {
            chrs.erase(i-1, 1);
          }
          hasPortals = true;
          break;
        } else {
          // Move surrounding chrs to start
          if(i != 0) {
            // Move letter before
            chrs.insert(0,string(1,chrs[i+1]));
            chrs.insert(0,string(1,chrs[i]));
            chrs.erase(i+3, 1);
            chrs.erase(i+1, 1);
          } else {
            // No letter before
            chrs.insert(0,string(1,chrs[i+1]));
            chrs.erase(i+2, 1);
          }
          hasPortals = true;
          break;
        }
        
        // cout << firstLetterI << " " << secondLetterI << "\n";
      }
    }  
  }

  if (!hasPortals) { // Not infinite
    cout << chrs << "\n";
  }
}