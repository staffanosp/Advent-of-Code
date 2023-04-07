import time
import copy



with open("input.txt","r") as file:
    boards = []
    current_board = []

    for i, line in enumerate([line.strip() for line in file]):
        if i == 0:  #first row
            numbers = [int(number) for number in line.split(",")]

        else:
            if not line:
                continue

            current_board.append([{'number':int(number), 'hit':False} for number in line.split()])

            if len(current_board) == 5:
                boards.append(current_board)
                current_board = []




def solution01(input_boards, numbers):
    boards = copy.deepcopy(input_boards)

    def bingo():
        for called_number_i, called_number in enumerate(numbers):
            #Mark hits
            for board_i, board in enumerate(boards):
                for row_i, row in enumerate(board):
                    for num_i, num in enumerate(row):
                        if num['number'] == called_number:
                            boards[board_i][row_i][num_i]['hit'] = True

            #Check for bingo
            if called_number_i > 3:   #skip check for the first 4 numbers
                for board_i, board in enumerate(boards):
                    if any(all(num['hit'] for num in row) for row in board) or any(all(num['hit'] for num in col) for col in zip(*board)):
                        return board_i, called_number
                     

    board_with_bingo, last_number_called = bingo()
    non_hit_numbers = []
    for row in boards[board_with_bingo]:
        for number in row:
            if not number['hit']:
                non_hit_numbers.append(number['number'])

    return sum(non_hit_numbers) * last_number_called


def solution02(input_boards, numbers):
    boards = copy.deepcopy(input_boards)

    def bingo():
        boards_with_bingo = []
        check_counter = 0
        for called_number_i, called_number in enumerate(numbers):
            #Mark hits
            for board_i, board in enumerate(boards):
                if board_i in [board[0] for board in boards_with_bingo]:
                    continue

                for row_i, row in enumerate(board):
                    for num_i, num in enumerate(row):
                        if num['number'] == called_number:
                            boards[board_i][row_i][num_i]['hit'] = True
        
            #Check for bingo
            if called_number_i > 3:   #skip check for the first 4 numbers
                for board_i, board in enumerate(boards):
                    if board_i in [board[0] for board in boards_with_bingo]:
                        continue

                    if any(all(num['hit'] for num in row) for row in board) or any(all(num['hit'] for num in col) for col in zip(*board)):
                        boards_with_bingo.append((board_i, called_number))
        
        return boards_with_bingo[-1] 


    last_board_with_bingo, number_called_at_last_bingo = bingo()
    non_hit_numbers = []
    for row in boards[last_board_with_bingo]:
        for number in row:
            if not number['hit']:
                non_hit_numbers.append(number['number'])

    return sum(non_hit_numbers) * number_called_at_last_bingo

solution01_start_time = time.time()
solution01 = solution01(boards, numbers)
solution01_total_time = time.time() - solution01_start_time
print(f"Solution 01: {solution01}, in {solution01_total_time}")

solution02_start_time = time.time()
solution02 = solution02(boards, numbers)
solution02_total_time = time.time() - solution02_start_time
print(f"Solution 02: {solution02}, in {solution02_total_time}")