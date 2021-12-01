// https://adventofcode.com/2021/day/1#part2

#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream cin("input.txt");
    int n, ans = 0;
    vector<int> nums;
    while (cin >> n) {
        nums.push_back(n);
    }
    for (int i = 3; i < nums.size(); i++) {
        int sum_left = nums[i-3] + nums[i-2] + nums[i-1];
        int sum_right = nums[i-2] + nums[i-1] + nums[i];
        if (sum_right > sum_left) ans++;
    }
    cout << ans << '\n';
    return 0;
}

