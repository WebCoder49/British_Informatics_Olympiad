// If you want to know how I got this solution, please email me at hi@webcoder49.dev .

#include <bits/stdc++.h>

using namespace std;

class PrimeFinder {
  vector<int> _primes;
  int _generatePrimesFrom = 2;

  public:
    void generatePrimes(int maxSquared) {
      int num;
      for(num = _generatePrimesFrom; num*num <= maxSquared; num++) {
        if(isPrime(num)) {
          _primes.push_back(num);
        }
      }
      _generatePrimesFrom = num;
    }

    bool isPrime(int num) {
      if(num < _generatePrimesFrom) {
        return find(_primes.begin(), _primes.end(), num) != _primes.end();
      }
      generatePrimes(num); // Up to square root so one from each pair of factors.
      for(int i = 0; i < _primes.size(); i++) {
        if(num % _primes[i] == 0) return false; // Not prime as divisible
        if(_primes[i]*_primes[i] > num) break; // Don't need to look further than sqrt
      }
      return true;
    }

    bool isCircularPrime(int num) {
      if(!isPrime(num)) {
        return false;
      }
      string numStr = to_string(num);
      for(int i = 0; i < numStr.size(); i++) {
        // Rotate string
        numStr = numStr.substr(1) + numStr[0];
        int rotation = 0;
        rotation = stoi(numStr);
        if(!isPrime(rotation)) {
          return false;
        }
      }

      return true;
    }
};

int main() {
  PrimeFinder primeFinder;
  int nextMin = 2;
  int count = 0;
  for(int i = 2; i < 1000000; i++) {
    if(primeFinder.isCircularPrime(i)) {
      count++;
    }
  }
  cout << "Count:" << count << "\n";
}