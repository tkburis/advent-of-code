// https://adventofcode.com/2021/day/1

#include <bits/stdc++.h>
using namespace std;

void part1(vector<int> nums)
{
    int prev, ans = 0;
    prev = nums[0];
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] > prev) ans++;
        prev = nums[i];
    }
    cout << "Part 1: " << ans << '\n';
}


void part2(vector<int> nums)
{
    int ans = 0;
    for (int i = 3; i < nums.size(); i++) {
        int sum_left = nums[i-3] + nums[i-2] + nums[i-1];
        int sum_right = nums[i-2] + nums[i-1] + nums[i];
        if (sum_right > sum_left) ans++;
    }
    cout << "Part 2: " << ans << '\n';
}

int main()
{
    ifstream cin("input.txt");
    vector<int> nums;
    int n;
    while (cin >> n) {
        nums.push_back(n);
    }
    part1(nums);
    part2(nums);
    return 0;
}

