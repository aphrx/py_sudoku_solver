import csv

class Board:
    def __init__(self, filename):
        self.board = self.parse_board(filename)
        
    def parse_board(self, filename):
        board = []
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                board.append(row)  
        return board

    def validate_board(self):
        vh = self.validate_horizontal()
        vv = self.validate_vertical()
        vs = self.validate_square()

        if vv and vs and vh:
            return True
        return False

    def validate_horizontal(self):
        for row in self.board:
            for i in range(1,10):
                if row.count(str(i)) > 1:
                    return False
        return True

    def validate_vertical(self):
        for col in range(9):
            temp = []
            for row in self.board:
                temp.append(row[col])
            for i in range(1,10):
                if temp.count(str(i)) > 1:
                    return False
        return True

    def validate_square(self):
        for sqr_col in range(3):
            for sqr_row in range(3):
                temp = []
                for sq_col in range(3):
                    for sq_row in range(3):
                        temp.append(self.board[sq_row + (3 * sqr_row)][sq_col + (3 * sqr_col)])
                
                for i in range(1,10):
                    if temp.count(str(i)) > 1:
                        return False
        return True

    def add(self, x, y, val):
        self.board[x][y] = str(val)
        return self.validate_board()

    def remove(self, x, y):
        self.board[x][y] = "0"
    
    def find_next_empty(self):
        for i_row, row in enumerate(self.board):
            for i_col, col in enumerate(row):
                if col == "0":
                    return i_row, i_col
        return -1, -1

    def cli(self):
        for row in self.board:
            temp = ""
            for ch in row:
                if ch == "0":
                    temp += f"- "
                else:
                    temp += f"{ch} "
            print(temp)
        print("\n")

if __name__ == "__main__":
    b = Board("/home/aphrx/Code/sudoku_solver/puzzles/sample-4.csv")
    print(b.validate_board())
    b.cli()
    print(b.add(7,5,9))
    b.cli()
    b.remove(7,5)
    b.cli()
    b.remove(7,4)
    b.cli()
    print(b.find_next_empty())
    b.cli()
