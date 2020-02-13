from unittest import TestCase
from typing import List


class Solution(object):
    def __init__(self, input_board: List[List[int]]):
        """
        :param input_board:
        """
        self.input_board = input_board
        # We want to assume that the input board is even by even
        if len(self.input_board) % 2 != 0:
            raise Exception('The board must have even rows and columns')
        if len(self.input_board) != len(self.input_board[0]):
            raise Exception('The board row length and column length must be the same')


    def movesToChessboard(self):
        """
        :type board: List[List[int]]
        :rtype: int
        """

    def is_chess_board(self, board: List[List[int]]):
        for row in board:
            if not self.is_valid_row_or_column(row):
                return False

    def is_pos_to_transform_to_chessboard(self):
        pass

    def get_cols_from_board(self, board: List[List[int]]):
        num_of_cols = board[0].__len__()
        output = []
        for col_num in range(num_of_cols):
            output.append([row[col_num] for row in board])
        return output

    @staticmethod
    def get_opposite_element_value(inp_value: int):
        if inp_value == 0:
            return 1
        elif inp_value == 1:
            return 0
        else:
            raise Exception('Unexpected input value ' + str(inp_value))

    @classmethod
    def is_valid_row_or_column(cls, col_or_row: List[int]):
        expected_next_element_value = col_or_row[0]
        for element in col_or_row:
            if element != expected_next_element_value:
                return False
            expected_next_element_value = cls.get_opposite_element_value(element)
        return True


class SolutionTest(TestCase):
    def setUp(self):
        self.input_board1 = [[0, 1, 1, 0],
                             [0, 1, 1, 0],
                             [1, 0, 0, 1],
                             [1, 0, 0, 1]]
        self.sol = Solution(self.input_board1)

    def test_is_chess_board(self):
        """ For now we just assume
        :return:
        """
        pass

    def test_get_cols_for_board(self):
        valid_output = [[0, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1]]
        seen_output = self.sol.get_cols_from_board(self.input_board1)
        self.assertEqual(seen_output, valid_output)

    def test_is_valid_row_or_column(self):
        inputs = [
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0,]]
        valid_outputs = [True, True, False, False, False]
        for i, inp in enumerate(inputs):
            self.assertEqual(Solution.is_valid_row_or_column(inp), valid_outputs[i])
