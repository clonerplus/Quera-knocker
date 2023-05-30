//
// Created by Cloner Plus on 2/23/22.
//
#include <iostream>
#include <string>
#include <cctype>
#include <algorithm>

void IsPalindrome(const std::string& sentence){

    std::string wantedSentence, reversed;

    for (char i : sentence){

        if (i != ' ' && !std::ispunct(i)){ wantedSentence += i;}

    }

    std::transform(wantedSentence.begin(), wantedSentence.end(), wantedSentence.begin(), ::tolower); // makes wantedSentence lowercase

    reversed = wantedSentence;

    std::reverse(reversed.begin(), reversed.end());

    if (wantedSentence == reversed) std::cout << "YES";

    else std::cout << "NO";

}

int main(){
    std::string string;
    std::getline(std::cin, string);

    IsPalindrome(string);
    return 0;
}
