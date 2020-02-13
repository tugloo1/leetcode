from typing import List
from unittest import TestCase

"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
"""


class Board(object):
    def __init__(self, board: List[List[int]]):
        self.board = board
        self.num_of_rows = len(board)
        self.num_of_cols = len(board[0])
        self.alive = 1
        self.dead = 0

    def __getitem__(self, item):
        if type(item) == tuple and len(item) != 2:
            raise Exception('fdsafsdafda')
        row, col = item
        if row < 0 or row >= self.num_of_rows:
            return None
        if col < 0 or col >= self.num_of_cols:
            return None
        value = self.board[row][col]
        if value == self.alive or value == 3:
            return self.alive
        else:
            return self.dead

    def get_num_of_neighbors_of_node(self, node_index) -> int:
        indicies = [-1, 0, 1]
        row, col = node_index
        num = 0
        for r in indicies:
            for c in indicies:
                if r == 0 and c == 0:
                    continue
                neighbor = self[row + r, col + c]
                if neighbor and neighbor == 1:
                    num += 1
        return num

    def apply_game_of_life(self):
        for row in range(self.num_of_rows):
            for col in range(self.num_of_cols):
                node_index = (row, col)
                if self[node_index] == self.alive:
                    neighbors = self.get_num_of_neighbors_of_node(node_index)
                    if neighbors < 2 or neighbors > 3:
                        self.board[row][col] = 3
                else:
                    if self.get_num_of_neighbors_of_node(node_index) == 3:
                        self.board[row][col] = 4

        for row in range(self.num_of_rows):
            for col in range(self.num_of_cols):
                if self.board[row][col] == 3:
                    self.board[row][col] = 0
                elif self.board[row][col] == 4:
                    self.board[row][col] = 1


class BoardTest(TestCase):
    def setUp(self):
        self.board = Board([[0, 1, 0],
                            [0, 0, 1],
                            [1, 1, 1],
                            [0, 0, 0]])

    def test_get_num_of_neighbors(self):
        self.assertEqual(self.board.get_num_of_neighbors_of_node((0, 0)), 1)
        self.assertEqual(self.board.get_num_of_neighbors_of_node((0, 1)), 1)
        self.assertEqual(self.board.get_num_of_neighbors_of_node((0, 2)), 2)

        self.assertEqual(self.board.get_num_of_neighbors_of_node((1, 0)), 3)
        self.assertEqual(self.board.get_num_of_neighbors_of_node((1, 1)), 5)
        self.assertEqual(self.board.get_num_of_neighbors_of_node((1, 2)), 3)

        self.assertEqual(self.board.get_num_of_neighbors_of_node((2, 0)), 1)
        self.assertEqual(self.board.get_num_of_neighbors_of_node((2, 1)), 3)
        self.assertEqual(self.board.get_num_of_neighbors_of_node((2, 2)), 2)

        self.assertEqual(self.board.get_num_of_neighbors_of_node((3, 0)), 2)
        self.assertEqual(self.board.get_num_of_neighbors_of_node((3, 1)), 3)
        self.assertEqual(self.board.get_num_of_neighbors_of_node((3, 2)), 2)

    def test_input1(self):
        self.board.apply_game_of_life()
        self.assertEqual([[0, 0, 0],
                          [1, 0, 1],
                          [0, 1, 1],
                          [0, 1, 0]], self.board.board)


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        b = Board(board)
        b.apply_game_of_life()
