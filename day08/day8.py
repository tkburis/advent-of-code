# https://adventofcode.com/2021/day/8

def part1(entries):
    ans = 0
    for entry in entries:
        for out in entry[1]:
            if len(out) in (2, 3, 4, 7):
                ans += 1
    print("Part 1:", ans)

def part2(entries):
    ans = 0
    for entry in entries:
        to_actual = {}
        to_code = {}
        char_sets = {}
        freqs = {}
        for i in range(7):
            freqs[chr(ord('a')+i)] = 0
        for inp in entry[0]:
            for c in inp:
                freqs[c] += 1
        a_or_c = set()
        d_or_g = set()
        for c, freq in freqs.items():
            if freq == 9:
                to_actual[c] = 'f'
                to_code['f'] = c
            elif freq == 6:
                to_actual[c] = 'b'
                to_code['b'] = c
            elif freq == 4:
                to_actual[c] = 'e'
                to_code['e'] = c
            elif freq == 8:
                a_or_c.add(c)
            elif freq == 7:
                d_or_g.add(c)
        one = set()
        four = set()
        seven = set()
        for inp in entry[0]:
            if len(inp) == 2:
                one = set(inp)
            elif len(inp) == 4:
                four = set(inp)
            elif len(inp) == 3:
                seven = set(inp)
        to_code['a'] = list(seven - one)[0]
        to_actual[to_code['a']] = 'a'
        to_code['c'] = list(a_or_c - set(to_code['a']))[0]
        to_actual[to_code['c']] = 'c'
        to_code['d'] = list(four - set(to_code['b'] + to_code['c'] + to_code['f']))[0]
        to_actual[to_code['d']] = 'd'
        to_code['g'] = list(d_or_g - set(to_code['d']))[0]
        to_actual[to_code['g']] = 'g'
        nums = {
            'abcefg': 0,
            'cf': 1,
            'acdeg': 2,
            'acdfg': 3,
            'bcdf': 4,
            'abdfg': 5,
            'abdefg': 6,
            'acf': 7,
            'abcdefg': 8,
            'abcdfg': 9
        }
        tot_num = ''
        for out in entry[1]:
            actual = [to_actual[x] for x in out]
            num = nums[''.join(sorted(actual))]
            tot_num += str(num)
        ans += int(tot_num)
    print(ans)

def main():
    with open("input.txt", "r") as f:
        entries = []
        for ln in f:
            ln = ln.split(' | ')
            left = ln[0].split()
            right = ln[1].split()
            entries.append([left, right])
    part1(entries)
    part2(entries)

if __name__ == "__main__":
    main()

