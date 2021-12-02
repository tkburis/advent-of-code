// https://adventofcode.com/2021/day/2

#include <bits/stdc++.h>
using namespace std;

void part1(vector<pair<string, int>> cmds)
{
    int depth = 0, horizontal = 0;
    for (auto p : cmds) {
        if (p.first == "forward") {
            horizontal += p.second;
        } else if (p.first == "down") {
            depth += p.second;
        } else if (p.first == "up") {
            depth -= p.second;
            depth = max(depth, 0);
        }
    }
    cout << "Part 1: " << depth * horizontal << '\n';
}

void part2(vector<pair<string, int>> cmds)
{
    int aim = 0, depth = 0, horizontal = 0;
    for (auto p : cmds) {
        if (p.first == "forward") {
            horizontal += p.second;
            depth += aim * p.second;
        } else if (p.first == "down") {
            aim += p.second;
        } else if (p.first == "up") {
            aim -= p.second;
        }
    }
    cout << "Part 2: " << depth * horizontal << '\n';
}

int main()
{
    ifstream cin("input.txt");
    vector<pair<string, int>> cmds;
    string in;
    while (cin >> in) {
        int n;
        cin >> n;
        cmds.push_back({in, n});
    }
    part1(cmds);
    part2(cmds);
    return 0;
}

