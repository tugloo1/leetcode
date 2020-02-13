from typing import List, Set
from unittest import TestCase


class GraphSolution(object):
    def __init__(self, graph: List[List[int]]):
        self.graph = graph
        self.nodes = len(graph)
        self.colors = [0] * len(graph)
        self.white, self.gray, self.black = 0, 1, 2

    def is_cycle_free(self, node):
        if self.colors[node] != self.white:
            return self.colors[node] == self.black

        self.colors[node] = self.gray
        for neighbor in self.graph[node]:
            if self.colors[neighbor] == self.black:
                continue
            if self.colors[neighbor] == self.gray:
                return False
            if not self.is_cycle_free(node):
                return False

        self.colors[node] = self.black
        return True


class Solution:
    @classmethod
    def eventualSafeNodes(cls, graph: List[List[int]]) -> List[int]:
        g = GraphSolution(graph)
        output = []
        for i in range(g.nodes):
            is_cycle = g.is_cycle_free(i)
            if not is_cycle:
                output.append(i)
        # a = g.is_cycle_free(1)
        return output



class SolutionTest(TestCase):
    def test_solution1(self):
        graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
        valid = [2, 4, 5, 6]
        self.assertEqual(Solution.eventualSafeNodes(graph), valid)

    def test_solution2(self):
        graph = [[0], [2, 3, 4], [3, 4], [0, 4], []]
        valid = [4]
        self.assertEqual(Solution.eventualSafeNodes(graph), valid)

    def test_solution3(self):
        graph = [[1, 2, 3, 4], [1, 2, 3, 4], [3, 4], [4], []]
        valid = [2, 3, 4]
        self.assertEqual(Solution.eventualSafeNodes(graph), valid)

    def test_solution4(self):
        graph = [[2, 3], [2, 3, 4], [3, 4], [], [1]]
        valid = [3]
        self.assertEqual(Solution.eventualSafeNodes(graph), valid)

    def test_solution5(self):
        graph = [[], [0, 2], [3], [1]]
        valid = [0]
        self.assertEqual(Solution.eventualSafeNodes(graph), valid)

