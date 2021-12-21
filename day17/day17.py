# https://adventofcode.com/2021/day/17

def hits(x_vel, y_vel, x1, x2, y1, y2):
    curr_x, curr_y = 0, 0
    maxi_y = 0
    while curr_x <= x2 and curr_y >= y1:
        curr_x += x_vel
        curr_y += y_vel
        if x_vel > 0:
            x_vel -= 1
        elif x_vel < 0:
            x_vel += 1
        y_vel -= 1
        maxi_y = max(maxi_y, curr_y)
        if y1 <= curr_y <= y2 and x1 <= curr_x <= x2:
            return True, maxi_y
    return False, 0
        

def part1(x1, x2, y1, y2):
    best = 0
    for x_vel in range(1, x2):
        for y_vel in range(1, -y1):
            res = hits(x_vel, y_vel, x1, x2, y1, y2)
            if res[0]:
                best = max(best, res[1])
    print('Part 1:', best)

def part2(x1, x2, y1, y2):
    vels = set()
    for x_vel in range(1, x2+1):
        for y_vel in range(y1, -y1):
            if hits(x_vel, y_vel, x1, x2, y1, y2)[0]:
                vels.add((x_vel, y_vel))
    print('Part 2:', len(vels))

def main():
    with open("input.txt", "r") as f:
        ln = f.readline().strip()
        ln = ln.split(': ')[1]
        xs, ys = ln.split(', ')
        x1, x2 = map(int, xs[2:].split('..'))
        y1, y2 = map(int, ys[2:].split('..'))
    part1(x1, x2, y1, y2)
    part2(x1, x2, y1, y2)

if __name__ == "__main__":
    main()

