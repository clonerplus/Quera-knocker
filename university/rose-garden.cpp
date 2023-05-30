// Powered by Clonerplus
#include <iostream>
#include <vector>
using namespace std;

int main() {
    string nm, month;
    int n, m;
    vector<char> r_l;
    getline(cin, nm);
    n = stoi(nm);
    r_l.reserve(n);
    for (int i = 0; i < n; i++){
        r_l.push_back('B');
    }
    nm.erase(nm.begin() + 0, nm.end() - 2);
    m = stoi(nm);
    for (int i = 0; i < m; i++){
        getline(cin, month);
        for (int j = 0; j < n; j++){
            if (month[j] == 'W'){
                if (r_l[j] == 'B'){
                    r_l[j] = 'F';
                } else {
                    r_l[j] = 'B';
                }
            }
        }
    }
    for (char i : r_l){
        cout << i;
    }
    return 0;
}
