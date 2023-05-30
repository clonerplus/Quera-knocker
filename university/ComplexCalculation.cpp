#include <iostream>
#include <cmath>

int factorial(int n) {
    if (n == 1 || n == 0) return 1;
    return n * factorial(n-1);
}

int cutFactorial(int n, int k) {
    int result = 1;
    for (int i = 0; i < n-k; n--){
        result *= n;
    }
    return result;
}

int main() {

    int n;
    long long a, x;
    unsigned long long result = 0;

    std::cin >> a >> x >> n;

    for (int k = 0; k < n+1; k++) {

        if (k > n-k) {
            result += (cutFactorial(n, k)/ factorial(n-k)) * pow(x, k) * pow(a, n-k);

        } else {
            result += (cutFactorial(n, n-k)/ factorial(k)) * pow(x, k) * pow(a, n-k);

        }

    } std::cout << result;

}
