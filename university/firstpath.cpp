#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <sstream>
#include <tuple>
using namespace std;

vector<long long> prime_list;
long long prime(long long x){
    if (count(prime_list.begin(), prime_list.end(), x)){
        return x;
    }
    if (x == 1){
        return 0;
    }
    for (int i = 1; i < 1+(pow(x, .5)); i+=1){
        if (x % i == 0){
            if ((x!=i) && (i!=1)){
                return 0;
            }
        }
    }
    prime_list.push_back(x);
    return x;
}

tuple<vector<vector<long long>>, vector<vector<long long>>> m(){
    vector<long long> small;
    vector<vector<long long>> medium, order;
    string line, num;
    int m;
    long long integer;
    stringstream ss;
    cin >> m;
    cin.ignore();
    for (int i = 0; i<m; ++i){
        getline(cin, line);
        ss << line;
        while (!ss.eof()){
            ss >> num;
            if (stringstream(num) >> integer){
                small.push_back(prime(integer));
            }
            num = "";
        }
        ss.str(string());
        ss.clear();
        medium.push_back(small);
        small.clear();
    }
    for (int i = 0; i<2; ++i){
        getline(cin, line);
        ss << line;
        while (!ss.eof()){
            ss >> num;
            if (stringstream(num) >> integer){
                small.push_back(integer);
            }
            num = "";
        }
        ss.str(string());
        ss.clear();
        order.push_back(small);
        small.clear();
    }
    return {order, medium};
}

void text(vector<vector<vector<long long>>> big){
    string path, pathc;
    long long s_row, s_column, e_row, e_column;
    for (int i = 0; i < big.size(); i+=2){
        path = "";
        s_row = big[i][0][0];
        s_column = big[i][0][1];
        e_row = big[i][1][0];
        e_column = big[i][1][1];
        while ((s_row != e_row) || (s_column != e_column)){
            pathc = path;
            big[i + 1][s_row][s_column] = 0;
            if (s_column+1 < big[i + 1].size()) {
                if (big[i + 1][s_row][s_column + 1] != 0) {
                    path += "R";
                    s_column++;
                    continue;
                }
            } if (s_column > 0) {
                if (big[i + 1][s_row][s_column - 1] != 0) {
                    path += "L";
                    s_column--;
                    continue;
                }
            } if (s_row+1 < big[i + 1].size()) {
                if (big[i + 1][s_row + 1][s_column] != 0) {
                    path += "D";
                    s_row++;\
                    continue;
                }
            } if (s_row > 0) {
                if (big[i + 1][s_row - 1][s_column] != 0) {
                    path += "U";
                    s_row--;
                    continue;
                }
            } if (pathc == path) {
                cout << "No Monaseb Masir!" << endl;
                break;
            }
        } if ((s_row == e_row) && (s_column == e_column)){
            cout << path << endl;
        }
    }
}

int main() {
    int n;
    vector<vector<vector<long long>>> big;
    tuple<vector<vector<long long>>, vector<vector<long long>>> result;
    cin >> n;
    big.reserve(n);
    for (int i = 0; i<n; i++){
        result = m();
        big.push_back(get<0>(result));
        big.push_back(get<1>(result));
    }
    text(big);
    return 0;
}