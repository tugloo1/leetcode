from typing import List
from unittest import TestCase


class MinRectangleFinder(object):
    def __init__(self, points: List[List[int]]):
        self.points = points
        self.min_area = 16*10**8 + 1
        self.x_hash, self.y_hash = self.create_hash_for_points()

    def create_hash_for_points(self):
        x_hash, y_hash = {}, {}
        for x, y in self.points:
            if x not in x_hash:
                x_hash[x] = set(y)
            else:
                x_hash[x].add(y)

            if y not in y_hash:
                y_hash[y] = set(x)
            else:
                y_hash[y].add(y)
        return x_hash, y_hash

    @staticmethod
    def get_area_between_points(point1: List[int, int], point2: List[int, int]):
        """ Assumes that point1 and point are diagonals
        :param point1:
        :param point2:
        :return:
        """
        x_width = abs(point1[0] - point2[0])
        y_width = abs(point1[1] - point2[1])
        return x_width * y_width

    def main_dfs_method(self):
        for point in self.points:
            direction = 'x'
            visited = [point]
            self.run_dfs_search(point, direction, [])

    @staticmethod
    def get_opposite_direction(direction: str):
        if direction == 'x':
            return 'y'
        elif direction == 'y':
            return 'x'
        else:
            raise Exception('nope')

    def run_dfs_search(self, next_point: List[int, int], direction: str, visited: List[List[int, int]]):
        visited.append(next_point)
        opposite_direction = self.get_opposite_direction(direction)
        # When we've seen 4 points
        if len(visited) == 4:
            first, third = visited[0], visited[2]
            area = self.get_area_between_points(first, third)
            self.min_area = min(area, self.min_area)
            return

        x, y = next_point[0], next_point[1]
        if direction == 'x':
            # Get all the points with the same x value as this guy
            possible_next_points = self.x_hash[x]
        elif direction == 'y':
            possible_next_points = self.y_hash[y]
        else:
            raise Exception('nope')

        for p in possible_next_points:
            self.run_dfs_search(p, opposite_direction, visited)
        visited.pop()




class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        pass


class SolutionTest(TestCase):
    pass
