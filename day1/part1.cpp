// https://adventofcode.com/2021/day/1

#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream cin("input.txt");
    int n, prev, ans = 0;
    cin >> n;
    prev = n;
    while (cin >> n) {
        if (n > prev) ans++;
        prev = n;
    }
    cout << ans << '\n';
    return 0;
}

