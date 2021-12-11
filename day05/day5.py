# https://adventofcode.com/2021/day/5

def part1(MAX_X, MAX_Y, segments):
    grid = [[0 for x in range(MAX_X)] for y in range(MAX_Y)]
    for segment in segments:
        x1 = segment[0][0]
        y1 = segment[0][1]
        x2 = segment[1][0]
        y2 = segment[1][1]
        if (x1 == x2):
            if (y1 > y2):
                y1, y2 = y2, y1
            for y in range(y1, y2+1):
                grid[y][x1] += 1
        elif (y1 == y2):
            if (x1 > x2):
                x1, x2 = x2, x1
            for x in range(x1, x2+1):
                grid[y1][x] += 1
    ans = 0
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if grid[y][x] >= 2:
                ans += 1
    print('Part 1:', ans)

def part2(MAX_X, MAX_Y, segments):
    grid = [[0 for x in range(MAX_X)] for y in range(MAX_Y)]
    for segment in segments:
        x1 = segment[0][0]
        y1 = segment[0][1]
        x2 = segment[1][0]
        y2 = segment[1][1]
        if (x1 == x2):
            if (y1 > y2):
                y1, y2 = y2, y1
            for y in range(y1, y2+1):
                grid[y][x1] += 1
        elif (y1 == y2):
            if (x1 > x2):
                x1, x2 = x2, x1
            for x in range(x1, x2+1):
                grid[y1][x] += 1
        else:
            xstep = -1 if x1 > x2 else 1
            ystep = -1 if y1 > y2 else 1
            ymod = -1 if y1 > y2 else 1
            curr_x = x1
            for y in range(y1, y2+ymod, ystep):
                grid[y][curr_x] += 1
                curr_x += xstep
    ans = 0
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if grid[y][x] >= 2:
                ans += 1
    print('Part 2:', ans)

def main():
    segments = []
    MAX_X = 0
    MAX_Y = 0
    with open("input.txt", "r") as f:
        for ln in f:
            ln = ln.split()
            left = list(map(int, ln[0].split(',')))
            right = list(map(int, ln[2].split(',')))
            for x in (left[0], right[0]):
                MAX_X = max(MAX_X, x)
            for y in (left[1], right[1]):
                MAX_Y = max(MAX_Y, y)
            segments.append([left, right])
    MAX_X += 1
    MAX_Y += 1
    part1(MAX_X, MAX_Y, segments)
    part2(MAX_X, MAX_Y, segments)

if __name__ == "__main__":
    main()

