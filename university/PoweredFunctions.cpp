//
// Created by Cloner Plus on 3/6/22.
//
#include <cstdio>
#include <cmath>

using namespace std;

long double MyPow(long double Base, unsigned int exp) {
    if (exp < 1) return pow(Base, exp);
    return Base * MyPow(Base, exp-1);
}

int main() {
    long double Base;
    unsigned int exp;
    scanf("%Lf%u", &Base, &exp);

    printf("%.3Lf", MyPow(Base, exp));
}
