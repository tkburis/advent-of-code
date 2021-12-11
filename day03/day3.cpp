// https://adventofcode.com/2021/day/3

#include <bits/stdc++.h>
using namespace std;

int LENGTH = 12;

void part1(vector<int> nums)
{
    int gamma = 0;
    for (int i = 0; i < LENGTH; i++) {
        int num0 = 0, num1 = 0;
        for (int num : nums) {
            if ((num >> (LENGTH - i - 1)) & 1) {
                num1++;
            } else {
                num0++;
            }
        }
        gamma <<= 1;
        if (num1 > num0) {
            gamma |= 1;
        }
    }
    int epsilon = pow(2, LENGTH) - 1 - gamma;
    cout << "Part 1: " << epsilon * gamma << '\n';
}

void part2(vector<int> nums)
{
    vector<int> o2_left(nums.begin(), nums.end()), co2_left(nums.begin(), nums.end());
    // o2
    int i = 0;
    while (o2_left.size() > 1 && i < LENGTH) {
        int num0 = 0, num1 = 0;
        vector<int> has0, has1;
        for (int j = 0; j < o2_left.size(); j++) {
            if ((o2_left[j] >> (LENGTH - i - 1)) & 1) {
                num1++;
                has1.push_back(o2_left[j]);
            } else {
                num0++;
                has0.push_back(o2_left[j]);
            }
        }
        i++;
        if (num1 >= num0) {
            for (int j : has0) {
                if (o2_left.size() > 1) {
                    o2_left.erase(remove(o2_left.begin(), o2_left.end(), j), o2_left.end());
                }
            }
        } else {
            for (int j : has1) {
                if (o2_left.size() > 1) {
                    o2_left.erase(remove(o2_left.begin(), o2_left.end(), j), o2_left.end());
                }
            }
        }
    }
    // co2
    i = 0;
    while (co2_left.size() > 1 && i < LENGTH) {
        int num0 = 0, num1 = 0;
        vector<int> has0, has1;
        for (int j = 0; j < co2_left.size(); j++) {
            if ((co2_left[j] >> (LENGTH - i - 1)) & 1) {
                num1++;
                has1.push_back(co2_left[j]);
            } else {
                num0++;
                has0.push_back(co2_left[j]);
            }
        }
        i++;
        if (num0 <= num1) {
            for (int j : has1) {
                if (co2_left.size() > 1) {
                    co2_left.erase(remove(co2_left.begin(), co2_left.end(), j), co2_left.end());
                }
            }
        } else {
            for (int j : has0) {
                if (co2_left.size() > 1) {
                    co2_left.erase(remove(co2_left.begin(), co2_left.end(), j), co2_left.end());
                }
            }
        }
    }
    cout << "Part 2: " << o2_left[0] * co2_left[0] << '\n';
}

int main()
{
    ifstream cin("input.txt");
    vector<int> all_nums;
    string in;
    while (getline(cin, in)) {
        int n = stoi(in, nullptr, 2);
        all_nums.push_back(n);
    }
    part1(all_nums);
    part2(all_nums);
    return 0;
}

