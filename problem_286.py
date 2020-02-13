from unittest import TestCase
from typing import List, Set, Tuple

"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the 
distance to a gate is less than 2147483647. Fill each empty room with the distance to its nearest gate. 
If it is impossible to reach a gate, it should be filled with INF.

"""


class ObstacleDist(object):
    def __init__(self, rooms: List[List[int]]):
        self.rooms = rooms
        self.rows = len(rooms)
        self.cols = len(rooms[0])

    def get_adjacent_nodes(self, node: Tuple[int, int]):
        row, col = node[0], node[1]
        left = row, col - 1
        right = row, col + 1
        up = row - 1, col
        down = row + 1, col
        for adj in [left, right, up, down]:
            if adj[0] < 0 or adj[0] >= self.rows:
                continue
            if adj[1] < 0 or adj[1] >= self.cols:
                continue
            yield adj

    def modify_with_closest_dist_to_gate(self):
        for row in range(self.rows):
            for col in range(self.cols):
                node = (row, col)
                node_val = self.rooms[row][col]
                if node_val == 0:
                    self.bfs_modify(node)

    def bfs_modify(self, node_with_gate: Tuple[int, int]):
        q = [node_with_gate]
        next_q = []
        visited = set()
        dist_from_gate = 1
        found_gate_with_smaller_dist = False
        while len(q) > 0:
            node = q.pop(0)
            visited.add(node)
            for adj_node in self.get_adjacent_nodes(node):
                if adj_node in visited:
                    continue
                row, col = adj_node[0], adj_node[1]
                node_val = self.rooms[row][col]
                if node_val == -1 or node_val == 0:
                    continue
                if node_val > dist_from_gate:
                    self.rooms[row][col] = dist_from_gate
                    found_gate_with_smaller_dist = True
                    next_q.append(adj_node)
            if q == []:
                if not found_gate_with_smaller_dist:
                    return
                q = next_q
                next_q = []
                dist_from_gate += 1
                found_gate_with_smaller_dist = False


class ObstacleDistTest(TestCase):
    def test_bfs_modify(self):
        obstacle_dist = ObstacleDist([[0, 100, 100, 100, 100, 0, 100, -1]])
        obstacle_dist.bfs_modify((0, 0))
        self.assertEqual([[0, 1, 2, 3, 4, 0, 100, -1]], obstacle_dist.rooms)
        obstacle_dist.bfs_modify((0, 5))
        self.assertEqual([[0, 1, 2, 2, 1, 0, 1, -1]], obstacle_dist.rooms)

    def test_1(self):
        input1 = [[2147483647,-1,0,2147483647],
                 [2147483647,2147483647,2147483647,-1],
                 [2147483647,-1,2147483647,-1],
                 [0,-1,2147483647,2147483647]]
        obstacle_dist = ObstacleDist(input1)
        obstacle_dist.modify_with_closest_dist_to_gate()
        correct = [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
        self.assertEqual(correct, obstacle_dist.rooms)
