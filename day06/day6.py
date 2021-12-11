# https://adventofcode.com/2021/day/6

def part1(init_state):
    curr_state = init_state.copy()
    for _ in range(80):
        for i in range(len(curr_state)):
            if curr_state[i] == 0:
                curr_state[i] = 6
                curr_state.append(8)
            else:
                curr_state[i] -= 1
    print('Part 1:', len(curr_state))

def part2(init_state):
    curr_state = init_state.copy()
    cnts = {x: 0 for x in range(9)}
    for x in curr_state:
        cnts[x] += 1
    # ## Possible optimisation for larger constraints: go up 7 days at a time instead, then do the last x % 7 separately
    # for _ in range(256//7):
    #     new_cnts = cnts.copy()
    #     for k, v in cnts.items():
    #         if 0 <= k <= 6:
    #             new_cnts[k+2] += v
    #         else:
    #             new_cnts[k%7] += v
    #             new_cnts[k] -= v
    #     cnts = new_cnts
    for _ in range(256):
        for k, v in cnts.items():
            if k == 0:
                cnts[0] -= v
                new_fish = v
            else:
                cnts[k] -= v
                cnts[k-1] += v
        cnts[6] += new_fish
        cnts[8] += new_fish
    print('Part 2:', sum(cnts.values()))

def main():
    with open("input.txt", "r") as f:
        init_state = list(map(int, f.readline().split(',')))
    part1(init_state)
    part2(init_state)

if __name__ == "__main__":
    main()

