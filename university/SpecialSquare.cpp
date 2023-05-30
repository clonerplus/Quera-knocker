//
// Created by Cloner Plus on 3/14/22.
//
#include <iostream>

int main() {
    int n = 7;

    std::cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i*j == 0 || i == j || i == n-1 || i+j == n-1 || (j >= n/2 && j > i && i+j >= n))
                std::cout << '#';
            else
                std::cout << ' ';
        } std::cout << '\n';
    }
}