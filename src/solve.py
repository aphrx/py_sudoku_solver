from board import Board
import argparse

class Solver:
    def __init__(self, args):
        self.board = Board(args.filename)

    def solve(self):
        x, y = self.board.find_next_empty()
        if x == -1 and y == -1:
            return self.board.cli()
        for i in range(1, 10):
            if self.board.add(x, y, i):
                self.solve()
            self.board.remove(x,y)
        
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="command line arguments")

    parser.add_argument(
        "--filename",
        type=str,
        required=True,
        help="sudoku filename",
    )
    args = parser.parse_args()
    s = Solver(args)
    s.solve()
