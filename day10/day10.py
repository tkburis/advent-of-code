# https://adventofcode.com/2021/day/10

def part1(lns, pr=True):
    ans = 0
    to_rm = []
    for i, ln in enumerate(lns):
        stack = []
        for c in ln:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif c == '<':
                stack.append('>')
            # elif c in (')', ']', '}', '>') and len(stack) == 0:
            #     break  # overcompleted line
            elif c in (')', ']', '}', '>') and stack[-1] != c:
                if c == ')':
                    ans += 3
                elif c == ']':
                    ans += 57
                elif c == '}':
                    ans += 1197
                elif c == '>':
                    ans += 25137
                to_rm.append(i)
                break
            else:  # its a closing bracket that matches the top of the stack
                stack.pop()
    if pr: print('Part 1:', ans)  # we dont have to print when this is called for second part, just to make it clean
    new_lns = [v for i, v in enumerate(lns) if i not in to_rm]
    return new_lns

def part2(lns):
    lns = part1(lns, pr=False)
    incompletes = []
    for ln in lns:
        stack = []
        for c in ln:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif c == '<':
                stack.append('>')
            # elif c in (')', ']', '}', '>') and len(stack) == 0:
            #     break  # overcompleted line
            # elif c in (')', ']', '}', '>') and stack[-1] != c:  # corrupted lines have been removed
            #     break
            else:
                stack.pop()
        if len(stack) > 0:
            score = 0
            for c in stack[::-1]:
                score *= 5
                if c == ')':
                    score += 1
                elif c == ']':
                    score += 2
                elif c == '}':
                    score += 3
                elif c == '>':
                    score += 4
            incompletes.append(score)
    incompletes = sorted(incompletes)
    print('Part 2:', incompletes[len(incompletes)//2])

def main():
    with open("input.txt", "r") as f:
        lns = [ln.strip() for ln in f]
    part1(lns)
    part2(lns)

if __name__ == "__main__":
    main()

