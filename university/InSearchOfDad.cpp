#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> primeList;

void primeNumberMaker() { // calculates a list of prime numbers lower than 1000
    primeList = {2};
    int currentNum = 3;
    while (currentNum < 1000){
        bool isPrime = true;
        for (auto i : primeList) {
            if (currentNum % i == 0){
                isPrime = false;
                break;
            }
        } if (isPrime) primeList.push_back(currentNum);
        currentNum++;
    }
}

int primeDecompositionSum(int n) { // decompositions the given number based on prime number list
    int result = 0;

    for (int i : primeList) {
        if (n % i == 0) {
            result += i;
            while (n % i == 0) n /= i;
        }
        if (n == 1) break;
    }
    return result;
}

int digitSum(int n) { // calculates digits sum of given number
    int result = 0;

    while (n > 0) {
        result += n % 10;
        n /= 10;
    }
    return result;
}

int D(int x) { // calculates dad of given x
    return primeDecompositionSum(x) + digitSum(x) + x;
}

int main() {
    int t, n;
    string toBePrinted;

    std::cin >> t;

    primeNumberMaker(); // makes primenumberslist

    vector<int> dads = {}; // calculates dads of x below 1000
    for (int i = 2; i < 1000; i++) {
        dads.push_back(D(i));
    }

    for (int i = 0; i < t; i++) {

        cin >> n;

        if (find(dads.begin(), dads.end(), n) != dads.end()) toBePrinted += "Yes\n";

        else toBePrinted += "No\n";

    }
    cout << toBePrinted;

}