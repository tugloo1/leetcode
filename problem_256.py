from typing import List
from unittest import TestCase


class PaintHouseSolver(object):
    def __init__(self, costs: List[List[int]]):
        self.costs = costs
        self.count = len(self.costs)
        self.min_cost = [costs[0]]
        # red blue green

    def solve(self):
        for i in range(1, self.count):
            current_house = self.costs[i]
            prior_house = self.min_cost[i-1]
            cost_of_red = current_house[0] + min(prior_house[1], prior_house[2])
            cost_of_blue = current_house[1] + min(prior_house[0], prior_house[2])
            cost_of_green = current_house[2] + min(prior_house[0], prior_house[1])
            self.min_cost.append([cost_of_red, cost_of_blue, cost_of_green])

        return min(self.min_cost[-1])


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        solver = PaintHouseSolver(costs)
        min_cost = solver.solve()
        return min_cost


class SolutionTest(TestCase):
    def testone(self):
        p = PaintHouseSolver( [[17,2,17],[16,16,5],[14,3,19]])
        answer = p.solve()
        self.assertEqual(answer, 10)
