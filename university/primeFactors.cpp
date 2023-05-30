// C program to illustrate the use of
// header file in C
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

vector<long long> primeList(long long n) { // prime numbers required to make decomposition
    vector<long long> list = {2};
    for (int i = 3; i <= (int) pow(n, .5); i+=2) {
        bool is = true;
        long long limit = i/2;
        for (long long j : list) {
            if (limit < j) break;
            if (i % j == 0){
                is = false;
                break;
            }

        } if (is) list.push_back(i);
    }

    return list;
}

long long orderCal(long long& num, long long i) { // divide until there is no more of i in num
    long long order = 0;
    while (num % i == 0) {
        num = num / i;
        order++;

    } return order;
}

void decomposition(long long num, const vector<long long>& candidates) { // makes wanted string of decomposition to print
    string answer = "";
    bool isPrime = true;
    for (auto i : candidates) {
        if (num < i) break;
        if (num % i == 0) {
            isPrime = false;
            long long order = orderCal(num, i);
            if (order == 1)
                answer += to_string(i) + '*';
            else
                answer += to_string(i) + '^' + to_string(order) + '*';
        }
    }
    if (isPrime) cout << num;

    else {
        if (num != 1) answer += to_string(num);

        else answer = answer.substr(0, answer.length()-1); // deletes the last unwanted "*"

        cout << answer;
    }




}

int main() {
    long long num;

    for (int i = 1; i < 2; i++) {
        cin >> num;
        vector<long long>candidates = primeList(num); // holds the decomposition candidates
        decomposition(num, candidates);
    }
}
