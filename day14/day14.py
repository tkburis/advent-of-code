# https://adventofcode.com/2021/day/14

from collections import Counter
from math import ceil

def part1(base, rules):
    curr = base
    for _ in range(10):
        new_curr = curr[0]
        for i in range(len(curr)-1):
            # if curr[i] + curr[i+1] in rules:  # guaranteed to be rule for every combination
            new_curr += rules[curr[i] + curr[i+1]]
            new_curr += curr[i+1]
        curr = new_curr
    cnts = Counter(curr)
    print('Part 1:', max(cnts.values()) - min(cnts.values()))

def part2(base, rules, distincts):
    pair_freqs = {d1+d2: 0 for d1 in distincts for d2 in distincts}
    for i in range(len(base)-1):
        pair_freqs[base[i]+base[i+1]] += 1

    for _ in range(40):
        new_pair_freqs = {d1+d2: 0 for d1 in distincts for d2 in distincts}
        for p, freq in pair_freqs.items():
            new_pair_freqs[p[0] + rules[p]] += freq
            new_pair_freqs[rules[p] + p[1]] += freq
        pair_freqs = new_pair_freqs
    cnts = {x: 0 for x in distincts}
    for p, freq in pair_freqs.items():
        cnts[p[0]] += freq
        cnts[p[1]] += freq
    print('Part 2:', ceil(max(cnts.values())/2) - ceil(min(cnts.values())/2))


def main():
    with open("input.txt", "r") as f:
        base = f.readline().strip()
        rules = {}
        distincts = set()
        for ln in f.readlines()[1:]:
            ln = ln.strip()
            ln = ln.split(' -> ')
            rules[ln[0]] = ln[1]
            distincts.update(ln[0])
            distincts.add(ln[1])
    part1(base, rules)
    part2(base, rules, distincts)

if __name__ == "__main__":
    main()

