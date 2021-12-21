# https://adventofcode.com/2021/day/21

def part1(p1_start, p2_start):
    dice = 1
    dice_rolled = 0
    p1_pos = p1_start
    p2_pos = p2_start
    p1_score = 0
    p2_score = 0
    while True:
        p1_pos += 3 * dice + 3
        p1_pos = (p1_pos - 1) % 10 + 1
        p1_score += p1_pos
        dice += 3
        dice = (dice - 1) % 100 + 1
        dice_rolled += 3
        if p1_score >= 1000:
            print('Part 1:', dice_rolled * p2_score)
            break
        p2_pos += 3 * dice + 3
        p2_pos = (p2_pos - 1) % 10 + 1
        p2_score += p2_pos
        dice += 3
        dice = (dice - 1) % 100 + 1
        dice_rolled += 3
        if p2_score >= 1000:
            print('Part 1:', dice_rolled * p1_score)
            break

def part2(p1_start, p2_start):
    ...

def main():
    with open("input.txt", "r") as f:
        p1_start = int(f.readline().strip().split(': ')[1])
        p2_start = int(f.readline().strip().split(': ')[1])
    part1(p1_start, p2_start)

if __name__ == "__main__":
    main()

