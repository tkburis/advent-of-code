# https://adventofcode.com/2021/day/11

def flash(cavern, y, x, flashed):
    new_cavern = cavern
    for dy in range(max(0, y-1), min(10, y+2)):
        for dx in range(max(0, x-1), min(10, x+2)):

            if new_cavern[dy][dx] <= 9 and (dy, dx) != (y, x):
                new_cavern[dy][dx] += 1

                if new_cavern[dy][dx] > 9:
                    flashed.append([dy, dx])
                    new_cavern = flash(new_cavern, dy, dx, flashed)
    return new_cavern

def part1(cavern):
    flashes = 0
    for _ in range(100):
        new_cavern = [[x+1 for x in row] for row in cavern]
        
        flashed = []
        for y in range(10):
            for x in range(10):
                if new_cavern[y][x] > 9 and [y, x] not in flashed:
                    new_cavern = flash(new_cavern, y, x, flashed)

        for y in range(10):
            for x in range(10):
                if new_cavern[y][x] > 9:
                    flashes += 1
                    new_cavern[y][x] = 0

        cavern = new_cavern
    print('Part 1:', flashes)

def part2(cavern):
    flashes = 0
    step = 1
    while True:
        new_cavern = [[x+1 for x in row] for row in cavern]
        
        flashed = []
        for y in range(10):
            for x in range(10):
                if new_cavern[y][x] > 9 and [y, x] not in flashed:
                    new_cavern = flash(new_cavern, y, x, flashed)

        cnt = 0
        for y in range(10):
            for x in range(10):
                if new_cavern[y][x] > 9:
                    flashes += 1
                    cnt += 1
                    new_cavern[y][x] = 0
                    
        if cnt == 100:
            print('Part 2:', step)
            break

        cavern = new_cavern
        step += 1

def main():
    with open("input.txt", "r") as f:
        cavern = [list(map(int, list(ln.strip()))) for ln in f]
    part1(cavern)
    part2(cavern)

if __name__ == "__main__":
    main()

