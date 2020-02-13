from typing import List
from unittest import TestCase
"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
"""


class Graph(object):
    def __init__(self, input_matrix: List[List[int]]):
        self.input_matrix = input_matrix
        self.rows = len(self.input_matrix)
        self.cols = len(self.input_matrix[0])

    def __getitem__(self, item):
        row, col = item
        return self.input_matrix[row][col]

    def finalize(self, should_zero_first_row:bool, should_zero_first_column):
        for row in range(1, self.rows):
            if self[row, 0] == 0:
                for col in range(1, self.cols):
                    self.input_matrix[row][col] = 0
                continue
            for col in range(1, self.cols):
                if self[0, col] == 0:
                    self.input_matrix[row][col] = 0
        if should_zero_first_row:
            for col in range(self.cols):
                self.input_matrix[0][col] = 0
        if should_zero_first_column:
            for row in range(self.rows):
                self.input_matrix[row][0] = 0

    def go_through(self):
        should_zero_first_row, should_zero_first_column = False, False
        if self[0, 0] == 0:
            should_zero_first_column, should_zero_first_row = True, True

        for col in range(self.cols):
            if self[0, col] == 0:
                should_zero_first_row = True
                break
        for row in range(self.rows):
            if self[row, 0] == 0:
                should_zero_first_column = True

        for row in range(1, self.rows):
            # If we encounter a row with 0 as the starting point, skip it
            for col in range(1, self.cols):
                if self[row, col] == 0:
                    self.input_matrix[row][0] = 0
                    self.input_matrix[0][col] = 0
        self.finalize(should_zero_first_row, should_zero_first_column)


class GraphTest(TestCase):
    def test1(self):
        input1 = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        valid_output = [[1, 0, 1],
                        [0, 0, 0],
                        [1, 0, 1]]
        graph = Graph(input1)
        graph.go_through()
        self.assertEqual(valid_output, graph.input_matrix)

    def test2(self):
        input1 = [[0, 1, 2, 0],
                  [3, 4, 5, 2],
                  [1, 3, 1, 5]]
        valid_output = [[0,0,0,0],
                        [0,4,5,0],
                        [0,3,1,0]]
        graph = Graph(input1)
        graph.go_through()
        self.assertEqual(valid_output, graph.input_matrix)

    def test3(self):
        input1 = [[8, 3, 6, 9, 7, 8, 0, 6],
                  [0, 3, 7, 0, 0, 4, 3, 8],
                  [5, 3, 6, 7, 1, 6, 2, 6],
                  [8, 7, 2, 5, 0, 6, 4, 0],
                  [0, 2, 9, 9, 3, 9, 7, 3]]
        expected = [[0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 3, 6, 0, 0, 6, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]]
        graph = Graph(input1)
        graph.go_through()
        self.assertEqual(expected, graph.input_matrix)


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        g = Graph(matrix)
        g.go_through()

