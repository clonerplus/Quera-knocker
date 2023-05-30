//
// Created by Cloner Plus on 3/7/22.
//
#include <iostream>
#include <bitset>

int main() {
    long n, binary = 1; // declared binary to hold the number which we need

    std::cin >> n;

    while(true) { // while binary form of the "binary" variable is less or equal to n
        if (std::stoi(std::bitset<30>(binary).to_string()) > n) break;
        binary++;
    }

    std::cout << binary-1;


}
