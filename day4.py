from day1 import get_mode


class Board:

    def __init__(self, id_, rows, columns, win):

        self.id_ = id_
        self.rows = rows
        self.columns = columns
        self.win = win

    def check_number(self, random_number):
        # if the random number is present, transform it to -1 both in rows and columns

        for row_index in range(len(self.rows)):
            for number_index in range(len(self.rows[row_index])):
                if self.rows[row_index][number_index] == random_number:
                    self.rows[row_index][number_index] = -1

        for column_index in range(len(self.columns)):
            for number_index in range(len(self.columns[column_index])):
                if self.columns[column_index][number_index] == random_number:
                    self.columns[column_index][number_index] = -1

    def check_victory(self):
        # a found number has become -1 because of check_number(), thus if the sum of a row (column) is
        # equal to minus its length, the board wins

        for row in self.rows:
            if sum(row) == -(len(row)):
                self.win = True

        for column in self.columns:
            if sum(column) == -(len(column)):
                self.win = True

    def compute_final_score(self, last_number):

        sum_ = 0

        for row in self.rows:
            for number in row:
                if number != -1:
                    sum_ += number

        result = sum_ * last_number

        return result


def compute_columns_from_rows(board_rows_int):

    board_columns_int = []

    for i in range(len(board_rows_int[0])):
        column = [row[i] for row in board_rows_int]
        board_columns_int.append(column)

    return board_columns_int


def open_file(path):

    with open(path, 'r') as f:
        lines = f.readlines()

    random_numbers = [int(number) for number in lines[0].split(',')]

    lines.remove(lines[0])  # remove the random numbers
    lines.remove(lines[0])  # remove the \n immediately after
    lines.append('\n')  # add a final \n to acquire also the last board

    board_list = []
    board_rows = []
    id_ = 0

    for row in lines:
        if row == '\n':
            # process the board acquired and reset everything for acquiring the next board

            board_rows_int = [list(map(int, row.strip().split())) for row in board_rows]  # clean each row and transform in int
            board_columns_int = compute_columns_from_rows(board_rows_int)

            board = Board(id_=id_, rows=board_rows_int, columns=board_columns_int, win=False)
            board_list.append(board)

            id_ += 1
            board_rows = []

        else:
            board_rows.append(row)

    return random_numbers, board_list


def main():

    path = "./data/input_day_4.txt"
    random_numbers, board_list = open_file(path)
    num_index = -1  # index for the random numbers

    mode = get_mode()

    if mode == 1:

        id_winner = -1
        win = False

        while not win:  # play the game until a board wins

            num_index += 1

            for board in board_list:
                board.check_number(random_numbers[num_index])
                board.check_victory()

                if board.win:
                    win = True
                    id_winner = board.id_
                    break

        for board in board_list:
            if board.id_ == id_winner:
                result = board.compute_final_score(random_numbers[num_index])

        print("ID of the win board:", id_winner)
        print("Final score:", result)

    elif mode == 2:

        id_last_winner = -1

        board_list_win = [board.win for board in board_list]
        num_of_boards = len(board_list)

        while board_list_win.count(True) < num_of_boards:

            num_index += 1

            for board in board_list:
                if not board.win:  # check only the boards that have not won yet
                    board.check_number(random_numbers[num_index])
                    board.check_victory()

                    if board.win and board_list_win.count(True) == num_of_boards - 1:  # if this is the last board to win
                        id_last_winner = board.id_

            board_list_win = [board.win for board in board_list]

        for board in board_list:
            if board.id_ == id_last_winner:
                result = board.compute_final_score(random_numbers[num_index])

        print("ID of the last win board:", id_last_winner)
        print("Final score:", result)


if __name__ == '__main__':
    main()
