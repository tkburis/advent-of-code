# https://adventofcode.com/2021/day/4

def check_win(board):
    # rows
    for row in board:
        if all(row):
            return True
    # cols
    for i in range(len(board[0])):
        col = [board[x][i] for x in range(len(board))]
        if all(col):
            return True

def part1(calls, boards):
    bool_boards = [[[False for c in row] for row in board] for board in boards]
    for call in calls:
        for curr_board in range(len(boards)):
            for i in range(len(boards[curr_board])):
                for j in range(len(boards[curr_board][0])):
                    if boards[curr_board][i][j] == call:
                        bool_boards[curr_board][i][j] = True
                        if check_win(bool_boards[curr_board]):
                            sum_unmarked = 0
                            for y in range(5):
                                for x in range(5):
                                    if bool_boards[curr_board][y][x] == False:
                                        sum_unmarked += boards[curr_board][y][x]
                            print('Part 1:', call * sum_unmarked)
                            return

def part2(calls, boards):
    won = [False for board in boards]
    bool_boards = [[[False for c in row] for row in board] for board in boards]
    # print(bool_boards)
    for call in calls:
        for curr_board in range(len(boards)):
            for i in range(len(boards[curr_board])):
                for j in range(len(boards[curr_board][0])):
                    if boards[curr_board][i][j] == call:
                        bool_boards[curr_board][i][j] = True
                        if check_win(bool_boards[curr_board]):
                            sum_unmarked = 0
                            for y in range(5):
                                for x in range(5):
                                    if bool_boards[curr_board][y][x] == False:
                                        sum_unmarked += boards[curr_board][y][x]
                            won[curr_board] = True
                            if all(won):
                                print('Part 2:', call * sum_unmarked)
                                return


def main():
    with open("input.txt", "r") as f:
        calls = list(map(int, f.readline().split(',')))
        # print(calls)
        boards = []
        while f.readline():
            board = []
            for _ in range(5):
                row = list(map(int, f.readline().split()))
                board.append(row)
            boards.append(board)
        # print(boards)
        part1(calls, boards)
        part2(calls, boards)

if __name__ == "__main__":
    main()

