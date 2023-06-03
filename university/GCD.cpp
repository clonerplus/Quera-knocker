#include "iostream"
#include "algorithm"

using namespace std;

//int MyPower(int x, int y) {
//    int result = 1;
//    for (int i = 0; i < y; i++) {
//        result *= x;
//    }
//}
//
//int MyPower2(int x, int y) {
//    if (y == 0) return 1;
//    return x * MyPower2(x, y-1);
//
//}

int main() {
    long a, b;
    cin >> a >> b;

    long c[3] = {a, b};
    sort(c, c+3);
//    cout << c[2] << endl << c[1] << endl << c[0];
    while (c[2] % c[1] != 0) {
        c[0] = c[2] % c[1];
        c[2] = c[1];
        c[1] = c[0];

    }
    cout << c[1];
    return 0;
}
