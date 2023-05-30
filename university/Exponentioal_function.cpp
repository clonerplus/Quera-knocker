//
// Created by Cloner Plus on 2/28/22.
//
#include <cstdio>
#include <cmath>

using namespace std;

int main(){
    long x, n, factorial = 1;
    double nMinusResult, result = 0;
    scanf("%li%li", &x, &n);

    for (long i = 0; i < n; i++){
        if (i != 0) factorial *= i;
        result += (double) pow(x, i) / factorial;
        if (isinf(result) || isnan(result)) break;
        else nMinusResult = result;
    }
    printf("%.3f", nMinusResult);


}

