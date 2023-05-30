#include <cstdio>
#include <cfloat>
#include <cmath>

using namespace std;

int main() {
    long n;
    scanf("%ld", &n);
    double input, max = -DBL_MAX, min = DBL_MAX, ave = 0.0;

    for (long i = 0; i < n; i++) {
        scanf(" %lg", &input);
        if (max < input) max = input;
        if (min > input) min = input;
        ave += input;


    } printf("Max: %.3lf\nMin: %.3lf\nAvg: %.3lf", floor(max * 1000) / 1000.0, floor(min * 1000) / 1000.0, floor(ave/n * 1000) / 1000.0);


    return 0;
}