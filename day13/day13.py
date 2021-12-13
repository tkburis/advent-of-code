# https://adventofcode.com/2021/day/13

def part1(dots, instruct, pr=True):
    new_dots = set()

    if instruct[0] == 'y':
        dots_above = set(dot for dot in dots if dot[0] < instruct[1])
        dots_below = set(dot for dot in dots if dot[0] > instruct[1])
        up_folded = set((instruct[1]*2 - dot[0], dot[1]) for dot in dots_below)
        new_dots = dots_above.union(up_folded)

    elif instruct[0] == 'x':
        dots_left = set(dot for dot in dots if dot[1] < instruct[1])
        dots_right = set(dot for dot in dots if dot[1] > instruct[1])
        left_folded = set((dot[0], instruct[1]*2 - dot[1]) for dot in dots_right)
        new_dots = dots_left.union(left_folded)

    if pr: print('Part 1:', len(new_dots))
    return new_dots

def part2(dots, instructs):
    curr_dots = dots
    for instruct in instructs:
        curr_dots = part1(curr_dots, instruct, pr=False)
    MAX_X = 0
    MAX_Y = 0
    for dot in curr_dots:
        MAX_X = max(MAX_X, dot[1])
        MAX_Y = max(MAX_Y, dot[0])
    grid = [['.' for x in range(MAX_X+1)] for y in range(MAX_Y+1)]
    for dot in curr_dots:
        grid[dot[0]][dot[1]] = '#'
    print('Part 2:')
    for row in grid: print(*(c if c != '.' else ' ' for c in row))

def main():
    dots = set()
    instructs = []
    with open("input.txt", "r") as f:
        d_input = True
        for ln in f:
            ln = ln.strip()
            if len(ln) == 0:
                d_input = False
                continue
            if d_input:
                x, y = map(int, ln.split(','))
                dots.add((y, x))
            else:
                ln = ln.split('=')
                axis = ln[0].split()[2]
                c = int(ln[1])
                instructs.append([axis, c])
    part1(dots, instructs[0])
    part2(dots, instructs)

if __name__ == "__main__":
    main()

