from typing import List
from unittest import TestCase


class Skyline(object):
    def __init__(self, skyline: List[List[int]]):
        self.skyline = skyline
        self.rows = len(self.skyline)
        self.cols = len(self.skyline[0])

    def solve(self):
        answer = 0
        max_rows = [0] * self.rows
        max_cols = [0] * self.cols
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                cell_value = self.skyline[i][j]
                if cell_value > max_rows[i]:
                    max_rows[i] = cell_value
                if cell_value > max_cols[j]:
                    max_cols[j] = cell_value

        for i in range(0, self.rows):
            for j in range(0, self.cols):
                if max_rows[i] < max_cols[j]:
                    smaller_value = max_rows[i]
                else:
                    smaller_value = max_cols[j]
                cell_value = self.skyline[i][j]
                if cell_value < smaller_value:
                    answer += smaller_value - cell_value
        return answer


class SolutionTest(TestCase):
    def test_solution(self):
        grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
        correct = 35
        skyline = Skyline(grid)
        self.assertEqual(skyline.solve(), correct)


