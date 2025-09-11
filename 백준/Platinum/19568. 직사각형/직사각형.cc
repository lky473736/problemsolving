#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<vector<int>> table(30, vector<int>(30, 0));

    for (int i = 0; i < 15; i++) {
        table[15][14 - i] = 1;
        table[14 - i][15] = 1 * 16;
        table[15][15 + i] = 1 * 16 * 16;
        table[15 + i][15] = 1 * 16 * 16 * 15;
        table[15][15] = 0;
    }

    for (int r = 0; r < 30; r++) {
        for (int c = 0; c < 30; c++) {
            cout << table[r][c] << " ";
        }
        cout << "\n";
    }

    return 0;
}
