from unittest import TestCase
from typing import List, Set, Tuple

"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
 Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
 Two cells are connected if they are adjacent cells connected horizontally or vertically.


"""


class CaptureSequence(object):
    def __init__(self, board: List[List[str]]):
        self.board = board
        self.rows = len(self.board)
        self.cols = len(self.board[0])

    def is_node_border_node(self, node: Tuple[int, int]):
        row_index, col_index = node[0], node[1]
        if row_index == 0 or row_index == self.rows - 1:
            return True
        if col_index == 0 or col_index == self.cols - 1:
            return True
        return False

    def get_adjacent_indicies(self, node: Tuple[int, int]):
        row_index, col_index = node[0], node[1]
        indicies = [(row_index - 1, col_index),
                    (row_index + 1, col_index),
                    (row_index, col_index - 1), (row_index, col_index + 1)]
        for i in indicies:
            row_index = i[0]
            col_index = i[1]
            if row_index < 0 or row_index == self.rows:
                continue
            if col_index < 0 or col_index == self.cols:
                continue
            yield i

    def capture_pawns(self):
        visited_zs = set()
        for row in range(1, self.rows - 1):
            for col in range(1, self.cols - 1):
                if self.board[row][col] == 'O' and (row, col) not in visited_zs:
                    node = (row, col)
                    sub_visited, valid_area = self.dfs_non_recursive(node)
                    if valid_area:
                        self.capture_area(sub_visited)
                    visited_zs.update(sub_visited)

    def dfs_non_recursive(self, starting_node) -> Tuple[Set[Tuple[int, int]], bool]:
        stack = [starting_node]
        visited = set()
        valid_area = True
        while len(stack) > 0:
            t_node = stack.pop() # Target Node
            if self.is_node_border_node(t_node):
                valid_area = False
            visited.add(t_node)
            for node in self.get_adjacent_indicies(t_node):
                if self.board[node[0]][node[1]] == 'O' and node not in visited:
                    stack.append(node)
        return visited, valid_area

    def capture_area(self, indices: Set):
        for index in indices:
            row, col = index[0], index[1]
            self.board[row][col] = 'X'


class SolutionTest(TestCase):
    def setUp(self):
        self.board_a = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ]

    def test_capture_area(self):
        board = CaptureSequence(self.board_a)
        board.capture_area({(1, 1), (1, 2)})
        valid_board = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ]
        self.assertEqual(board.board, valid_board)

    def test_is_node_border_node(self):
        board = CaptureSequence(self.board_a)
        self.assertTrue(board.is_node_border_node((0, 0)))
        self.assertTrue(board.is_node_border_node((0, 1)))
        self.assertTrue(board.is_node_border_node((0, 3)))
        self.assertTrue(board.is_node_border_node((2, 3)))
        self.assertTrue(board.is_node_border_node((3, 3)))
        self.assertTrue(board.is_node_border_node((3, 0)))
        self.assertFalse(board.is_node_border_node((1, 1)))
        self.assertFalse(board.is_node_border_node((1, 2)))
        self.assertFalse(board.is_node_border_node((2, 2)))

    def test_sample_one(self):
        board = CaptureSequence(self.board_a)
        expected = [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","O","X","X"]]
        board.capture_pawns()
        self.assertEqual(expected, board.board)
