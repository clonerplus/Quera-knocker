#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

map<unsigned long long, unsigned long long> tiles;

void tile_manager(vector<unsigned long long> order){
    unsigned long long m = order[0], n = order[1];
    if (m == 0) return;
    if (m == 1) {
        if (::tiles.count(1)){
            tiles[1] += n;
        } else {
            tiles[1] = n;
        } return;
    }
    unsigned long long a = 1, b;
    for (unsigned long long i = 1; i <= 8*28; i++) {
        a = 1 << i;
        if (a > m) {
            a = 1 << (i-1);
            break;
        }
    }
    b = n/a;
    tile_manager({m-a, b*a});
    tile_manager({n-(b*a), m});
    if (::tiles.count(a)) ::tiles[a] += b;
    else ::tiles[a] = b;
}

int main() {
    vector<unsigned long long> order;
    unsigned long long m, n;
    cin >> m >> n;
    order.push_back(min(m, n));
    order.push_back(max(m, n));
    tile_manager(order);


    for (auto i = ::tiles.rbegin(); i != ::tiles.rend(); i++){
        cout << i->second << ' ' << i->first << "*" << i->first << " tiles" << endl;
    }
    return 0;
}
