# https://adventofcode.com/2021/day/7

def part1(all_pos):
    all_pos = sorted(all_pos)
    med = all_pos[len(all_pos)//2]
    print('Part 1:', sum(abs(x - med) for x in all_pos))

def part2(all_pos):
    best = 1000000000000
    for med in range(1, max(all_pos)):
        s = 0
        for pos in all_pos:
            s += (abs(pos - med) * (abs(pos - med) + 1)) // 2
        best = min(s, best)
    print('Part 2:', best)

def main():
    with open("input.txt", "r") as f:
        all_pos = list(map(int, f.readline().split(',')))
    part1(all_pos)
    part2(all_pos)

if __name__ == "__main__":
    main()

