#include <bits/stdc++.h>
using namespace std;

/*
1
11
111
121
1211
1221
12211
12221
12321
123211
123221
123321

거리 / 장치작동횟수
1 - 1
2 - 2
3,4 - 3
5,6 - 4
7,8,9 - 5
10,11,12 - 6
...

최소워프값이 최대거리-제곱근+1
최소워프값은 제곱근 *2 - 1

*/

int main() {
    long long t;
    cin >> t;

    while (t-- > 0) {
        long long s, f;
        cin >> s >> f;

        long long dis = f - s;
        long long sqrt_dis = (long long)std::ceil(std::sqrt(dis));
        long long max_square = sqrt_dis * sqrt_dis;

        if (max_square - sqrt_dis >= dis) {
            cout << sqrt_dis * 2 - 2 << '\n';
        } else {
            cout << sqrt_dis * 2 - 1 << '\n';
        }
    }

    return 0;
}
