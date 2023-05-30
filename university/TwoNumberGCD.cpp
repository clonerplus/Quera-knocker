#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    long a, b;
    cin >> a >> b;

    long c[3] = {a, b}; // keeps track of rem, divisor, divided
    sort(c, c+3);

    while (c[2] % c[1] != 0) { // while finding the right divisor according to euclid
        c[0] = c[2] % c[1]; // finding the remainder
        c[2] = c[1]; // change divided and divisor
        c[1] = c[0]; // change divisor and remainder

    }

    cout << c[1];

    return 0;
}