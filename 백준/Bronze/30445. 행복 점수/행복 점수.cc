#include <bits/stdc++.h>

using namespace std;

bool ph[26];
bool ps[26];

int ctoi(char &s)
{
    return s - 'A';
}

int main()
{
    string st;
    getline(cin, st);
    ph[0] = true;
    ph[7] = true;
    ph[15] = true;
    ph[24] = true;

    ps[0] = true;
    ps[3] = true;
    ps[18] = true;
    double h = 0, s = 0;
    for (auto c : st)
    {
        if (c == ' ')
            continue;
        int temp = ctoi(c);
        if (ph[temp])
            h++;
        if (ps[temp])
            s++;
    }
    cout << fixed << setprecision(2);
    if (h + s == 0)
        cout << "50.00";
    else
        cout << round((h / (h + s)) * 10000) / 100;
}