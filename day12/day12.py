# https://adventofcode.com/2021/day/12

from queue import Queue

def part1(adj):
    q = Queue()
    q.put(('start', ['start']))
    all_paths = 0
    while (not q.empty()):
        curr = q.get()
        curr_node = curr[0]
        curr_path = curr[1]
        already_small_caves = set(x for x in curr_path if x.islower())
        for neighbour in adj[curr_node]:
            if neighbour == 'end':
                all_paths += 1
            elif neighbour != 'start' and neighbour not in already_small_caves:
                q.put((neighbour, curr_path+[neighbour]))
    print('Part 1:', all_paths)

def part2(adj):
    q = Queue()
    q.put(('start', ['start']))
    all_paths = 0
    while (not q.empty()):
        curr = q.get()
        curr_node = curr[0]
        curr_path = curr[1]

        can_twice = 2 not in set(curr_path.count(x) for x in set(curr_path) if x.islower())  # has a small cave NOT already been visited twice? (i.e. we can visit a small cave twice now)
        if can_twice:
            can_small_caves = set(x for x in adj[curr_node] if x.islower() and x != 'start')  # if we can, then we can go to any small cave we want
        else:
            can_small_caves = set(x for x in adj[curr_node] if x not in curr_path and x.islower() and x != 'start')  # if not, then we can only go to small caves we have not visited yet
        can_caves = can_small_caves.union(set(x for x in adj[curr_node] if x.isupper()))

        for neighbour in adj[curr_node]:
            if neighbour == 'end':
                all_paths += 1
            elif neighbour in can_caves:
                q.put((neighbour, curr_path+[neighbour]))
    print('Part 2:', all_paths)

def main():
    adj = {}
    with open("input.txt", "r") as f:
        for ln in f:
            left = ln.strip().split('-')[0]
            right = ln.strip().split('-')[1]
            if left not in adj:
                adj[left] = []
            if right not in adj:
                adj[right] = []
            adj[left].append(right)
            adj[right].append(left)
    part1(adj)
    part2(adj)

if __name__ == "__main__":
    main()

