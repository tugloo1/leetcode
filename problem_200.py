from unittest import TestCase
from typing import List, Set
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""


class IslandFinder(object):
    def __init__(self, input_island: List[List[str]]):
        self.island = input_island
        self.rows = len(self.island)
        self.cols = len(self.island[0])

    def determine_num_of_islands(self):
        islands = 0
        full_visited = set()
        for i in range(self.rows):
            for j in range(self.cols):
                node = (i, j)
                if self.island[i][j] == '1' and node not in full_visited:
                    sub_visited = set()
                    o = self.dfs_recursive_island_search(sub_visited, node)
                    if o:
                        islands += 1
                        full_visited = full_visited.union(o)
        return islands

    def get_adjacent_indicies(self, row_index: int, col_index: int):
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

    def dfs_recursive_island_search(self, visited: Set, node_to_eval):
        visited.add(node_to_eval)
        for node in self.get_adjacent_indicies(node_to_eval[0], node_to_eval[1]):
            if node not in visited and self.island[node[0]][node[1]] == '1':
                self.dfs_recursive_island_search(visited, node)
        return visited


class IslandFinderTest(TestCase):
    def test_get_adjacent_indices(self):
        a = [
            [1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        island_finder = IslandFinder(a)
        self.assertEqual(set(island_finder.get_adjacent_indicies(0, 0)), {(0, 1), (1, 0)})
        self.assertEqual(set(island_finder.get_adjacent_indicies(0, 1)), {(0, 0), (0, 2), (1, 1)})
        self.assertEqual(set(island_finder.get_adjacent_indicies(0, 4)), {(0, 3), (1, 4)})
        self.assertEqual(set(island_finder.get_adjacent_indicies(2, 2)), {(2, 1), (2, 3), (1, 2), (3, 2)})
        self.assertEqual(set(island_finder.get_adjacent_indicies(2, 3)), {(2, 2), (2, 4), (1, 3), (3, 3)})
        self.assertEqual(set(island_finder.get_adjacent_indicies(3, 4)), {(3, 3), (2, 4)})

    def test_1(self):
        a = [
            ['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']
        ]
        island_finder = IslandFinder(a)
        self.assertEqual(island_finder.determine_num_of_islands(), 1)

        pass

    def test_2(self):
        a = [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']
        ]
        island_finder = IslandFinder(a)
        self.assertEqual(island_finder.determine_num_of_islands(), 3)

