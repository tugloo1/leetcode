from typing import List
from unittest import TestCase


class OrangeManager(object):
    empty = 0
    fresh = 1
    rotten = 2

    def __init__(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def get_fresh_neighbor_oranges(self, row, col):
        left, right, top, down = (row, col - 1), (row, col + 1), (row - 1 , col), (row + 1, col)
        ns = [left, right, top, down]
        to_return = []
        for n in ns:
            row, col = n
            if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.grid[row][col] != 1:
                continue
            to_return.append(n)
        return to_return

    def how_long_to_spoil(self):
        main_set, next_set = set(), set()
        minutes_passed = 0
        num_fresh = 0

        for row in range(self.rows):
            for col in range(self.cols):
                cell = (row, col)
                orange = self.grid[row][col]
                if orange == self.fresh:
                    num_fresh += 1
                elif orange == self.rotten:
                    main_set.add(cell)

        while main_set:
            for rotten_orange in main_set:
                row, col = rotten_orange
                neighbors = self.get_fresh_neighbor_oranges(row, col)
                for n in neighbors:
                    if n not in main_set:
                        self.grid[row][col] = self.rotten
                        next_set.add(n)
            if next_set:
                minutes_passed += 1
            num_of_new_rotten_oranges = len(next_set)
            num_fresh -= num_of_new_rotten_oranges
            main_set = next_set
            next_set = set()

        if num_fresh > 0:
            return -1
        return minutes_passed


class SolutionTestCase(TestCase):
    def test_one(self):
        s = OrangeManager([[2,1,1],[1,1,0],[0,1,1]])
        self.assertEqual(s.how_long_to_spoil(), 4)

    def test_two(self):
        s = OrangeManager([[2,1,1],[0,1,1],[1,0,1]])
        self.assertEqual(s.how_long_to_spoil(), -1)

    def test_three(self):
        s = OrangeManager([[0,2]])
        self.assertEqual(s.how_long_to_spoil(), 0)

    def test_four(self):
        s = OrangeManager([[1],[2],[1],[2]])
        self.assertEqual(s.how_long_to_spoil(), 1)

    def test_five(self):
        s = OrangeManager([[2,2],[1,1],[0,0],[2,0]])
        self.assertEqual(s.how_long_to_spoil(), 1)