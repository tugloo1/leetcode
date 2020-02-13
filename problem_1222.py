from unittest import TestCase
from typing import List, Tuple
from queue import Queue


class Solution(object):
    @staticmethod
    def is_valid_pos(pos: Tuple[int, int]):
        for i in pos:
            if i < 0 or i > 7:
                return False
        return True

    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        queue = Queue()
        queen_set = set()
        for q in queens:
            queen_set.add(tuple(q))
        x_king, y_king = king[0], king[1]
        increments = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        # Starting
        for i_x, i_y in increments:
            new_pos = (x_king + i_x, y_king + i_y)
            info = (new_pos, (i_x, i_y))
            queue.put(info)

        valid_queens = []
        while not queue.empty():
            pos, increment = queue.get()
            if not self.is_valid_pos(pos):
                continue
            if pos in queen_set:
                valid_queens.append(list(pos))
                continue
            new_pos_x = pos[0] + increment[0]
            new_pos_y = pos[1] + increment[1]
            new_pos = (new_pos_x, new_pos_y)
            info = (new_pos, increment)
            queue.put(info)

        return valid_queens


class SolutionTest(TestCase):
    def dummy_assert(self, list1: List[List[int]], list2:List[List[int]]):
        self.assertEqual(len(list1), len(list2))
        for i in list1:
            self.assertIn(i, list2)

    def tests(self):
        sol = Solution()
        queens = [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]]
        king = [0, 0]
        self.dummy_assert([[0,1],[1,0],[3,3]], sol.queensAttacktheKing(queens, king))

        queens = [[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]]
        king = [3, 3]
        self.dummy_assert([[2,2],[3,4],[4,4]], sol.queensAttacktheKing(queens, king))

        queens = [[5, 6], [7, 7], [2, 1], [0, 7], [1, 6], [5, 1], [3, 7], [0, 3], [4, 0], [1, 2], [6, 3], [5, 0],
                  [0, 4], [2, 2], [1, 1], [6, 4], [5, 4], [0, 0], [2, 6], [4, 5], [5, 2], [1, 4], [7, 5], [2, 3],
                  [0, 5], [4, 2], [1, 0], [2, 7], [0, 1], [4, 6], [6, 1], [0, 6], [4, 3], [1, 7]]
        king = [3, 4]
        self.dummy_assert([[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]], sol.queensAttacktheKing(queens, king))
