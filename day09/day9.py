# https://adventofcode.com/2021/day/9
from queue import Queue

def part1(locs, pr=True):
    ans = 0
    low_points = []
    for y in range(len(locs)):
        for x in range(len(locs[0])):
            ok = True
            if y > 0:
                if locs[y-1][x] <= locs[y][x]:
                    ok = False
            if y < len(locs)-1:
                if locs[y+1][x] <= locs[y][x]:
                    ok = False
            if x > 0:
                if locs[y][x-1] <= locs[y][x]:
                    ok = False
            if x < len(locs[0])-1:
                if locs[y][x+1] <= locs[y][x]:
                    ok = False
            if ok:
                ans += locs[y][x]+1
                low_points.append([y, x])
    if pr: print('Part 1:', ans)  # we don't have to print when part1() is called in part2()
    return low_points

def part2(locs):
    low_points = part1(locs, pr=False)
    max_three = [0, 0, 0]
    for src in low_points:
        vis = []
        q = Queue()
        q.put(src)
        vis.append(src)
        while (not q.empty()):
            y, x = q.get()
            deltas = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for delta in deltas:
                dy, dx = y + delta[0], x + delta[1]
                if dy < 0 or dy > len(locs)-1 or dx < 0 or dx > len(locs[0])-1 or [dy, dx] in vis:
                    continue
                if locs[dy][dx] == 9 or locs[dy][dx] <= locs[y][x]:
                    continue
                q.put([dy, dx])
                vis.append([dy, dx])
        if any(len(vis) > k for k in max_three):
            max_three[max_three.index(min(max_three))] = len(vis)
    ans = 1
    for m in max_three:
        ans *= m
    print('Part 2:', ans)

def main():
    with open("input.txt", "r") as f:
        locs = []
        for ln in f:
            locs.append(list(map(int, list(ln.strip()))))
    part1(locs)
    part2(locs)

if __name__ == "__main__":
    main()

