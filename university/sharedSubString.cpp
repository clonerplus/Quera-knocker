#include <iostream>
#include <cstring>
#include <algorithm>

bool containStr(char* bigger, char* smaller) { // checks two strings if one is the sub string of another returns true
    bool contains;

    for (int i = 0; i <= strlen(bigger) - strlen(smaller); i++) { // checks the strings char by char
        contains = true;
        for (int j = 0; j < strlen(smaller); j++){
            if (bigger[i + j] != smaller[j]) {
                contains = false;
                break;
            }

        } if (contains) {
            return true;
        }

    } return false;
}

bool checkString(char (*p)[21], char c[], int n) { // checks substring candidate by all the input strings
    bool isFound = true;

    char reverse[21]; // holds the reverse form of "c" candidate
    memcpy(reverse, c, strlen(c));
    reverse[strlen(c)] = '\0';
    std::reverse(reverse, reverse + strlen(c));

    for (int j = 0; j < n; j++) { // checks if all the inputs contain this candidate or the reverse form
        if (!containStr(*(p+j), c) && !containStr(*(p+j), reverse)) {
            isFound = false;
            break;
        }
    } return isFound;
}

void sharedString(char (*p)[21], char* shared, int n) {
    char result[21] = ""; // holds the final result
    char c[21]; // holds the candidates for being experimented as substring
    memcpy(c, shared, 21);
    unsigned long length = strlen(c);

    for (int i = 0; i < length; i++) {
        for (int j = 0; j < length - i; j++) {
            memcpy(c, shared + i, length - i - j); // copies the substring of the shortest string into c
            c[length - i - j] = '\0';

            if (checkString(p, c, n)) { // if the candidate is actually a substring
                if (strlen(result) < strlen(c)) {
                    memcpy(result, c, strlen(c));
                    result[strlen(c)] = '\0';
                }
                break;
            }
        }
    }
    if (containStr(*p, result)) // detains the order of result to be as the first input
        std::cout << result;

    else{
        std::reverse(result, result + strlen(result));
        std::cout << result;
    }

}

int main() {
    int n;
    std::cin >> n;

    char (*shared)[21]; // holds the pointer to the shortest input
    char inputs[n][21];


    std::cin >> inputs[0];
    shared = &inputs[0];


    for (int i = 1; i < n; i++) { // finds the shortest string
        std::cin >> inputs[i];
        if (strlen(*shared) > strlen(inputs[i])) shared = &inputs[i];
    }

    sharedString(inputs, *shared, n);

    return 0;
}