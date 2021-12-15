# https://adventofcode.com/2021/day/15

from queue import PriorityQueue

def part1(grid, pr=True):
    dist = {(y, x): float('inf') for y in range(len(grid)) for x in range(len(grid[0]))}
    dist[(0, 0)] = 0
    vis = {(y, x): False for y in range(len(grid)) for x in range(len(grid[0]))}

    pq = PriorityQueue()
    pq.put((0, (0, 0)))

    while not pq.empty():
        (curr_dist, (y, x)) = pq.get()
        vis[(y, x)] = True
        for (dy, dx) in ((y+1, x), (y-1, x), (y, x+1), (y, x-1)):
            if 0 <= dy < len(grid) and 0 <= dx < len(grid[0]) and vis[(dy, dx)] == False:
                old_dist = dist[(dy, dx)]
                new_dist = dist[(y, x)] + grid[dy][dx]
                if new_dist < old_dist:
                    pq.put((new_dist, (dy, dx)))
                    dist[(dy, dx)] = new_dist

    res = dist[(len(grid)-1, len(grid[0])-1)]
    if pr: print('Part 1:', res)
    return res

def part2(grid): 
    big_grid = [[] for _ in range(5*len(grid))]
    for i, row in enumerate(grid):  # make first 'big' row
        for add in range(5):
            big_grid[i].extend([(x+add-1)%9+1 for x in row])
    for i in range(len(grid), 5*len(grid)):
        big_grid[i] = [x%9+1 for x in big_grid[i-len(grid)]]
    print('Part 2:', part1(big_grid, pr=False))

def main():
    grid = []
    with open("input.txt", "r") as f:
        for ln in f:
            grid.append(list(map(int, list(ln.strip()))))
    part1(grid)
    part2(grid)

if __name__ == "__main__":
    main()

