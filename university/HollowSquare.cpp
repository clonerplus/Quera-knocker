//
// Created by Cloner Plus on 3/6/22.
//

#include "iostream"
#include "cstring"

using namespace std;

int main() {
    int a, b;

    cin >> a >> b;

    if (!(a > b)) {
        cout << "Wrong order!";
        return 0;
    }

    if ((a - b) % 2 != 0) {
        cout << "Wrong difference!";
        return 0;
    }

    for (int i = 0; i < a; i++) {
        if (i >= (a-b)/2 && i < (a-b)/2 + b) {
            for (int j = 0; j < (a-b)/2; j++) {
                cout << "* ";
            }

            for (int j = 0; j < b; j++) {
                cout << "  ";
            }

            for (int j = 0; j < (a-b)/2; j++) {
                cout << "* ";
            }

        } else {
            for (int j = 0; j < a; j++) {
                cout << "* ";
            }
        }
        cout << "\n";
    }


}
