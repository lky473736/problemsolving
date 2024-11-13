#include <bits/stdc++.h>
using namespace std;

string arr[500001];
bool used[500001];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, k, m, f;
    cin >> n >> k >> m >> f;
    int in;
    for (int q = 0; q < k; q++)
    {
        for (int w = 0; w < m; w++)
        {
            cin >> in;
            if (!used[in])
            {
                arr[in] += "1";
                used[in] = true;
            }
        }
        for (int i = 1; i <= n; i++)
        {
            if (!used[i])
                arr[i] += "0";
        }

        fill(used, used + n + 1, false);
    }
    vector<bitset<100>> v(n);
    for (int i = 1; i <= n; i++)
    {
        bitset<100> bit(arr[i]);
        v[i - 1] = bit;
    }
    unordered_map<bitset<100>, int> dic;
    for (int i = 1; i <= n; i++)
    {
        if (dic.find(v[i - 1]) != dic.end())
            dic[v[i - 1]] = -1;
        else
            dic[v[i - 1]] = i;
    }
    for (int i = 0; i < f; i++)
    {
        string str;
        string find_num = "";
        cin >> str;
        for (int j = 0; j < k; j++)
        {
            if (str[j] == 'Y')
                find_num += "1";
            else
                find_num += "0";
        }
        // cout << find_num << '\n';
        bitset<100> num(find_num);
        int result = dic[num];
        if (result == -1)
            result = 0;
        cout << result << '\n';
    }
    return 0;
}