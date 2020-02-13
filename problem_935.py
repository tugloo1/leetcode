from unittest import TestCase


class Solution:
    @staticmethod
    def knightDialer(n: int) -> int:
        keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        pos_map = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [4, 2],
        }
        start_count = {k: 1 for k in keys}
        hops_completed = 1

        while hops_completed < n:
            new_count = {k: 0 for k in keys}
            for k in keys:
                pos = start_count[k]
                paths = pos_map[k]
                for path in paths:
                    new_count[path] += pos
            start_count = new_count
            hops_completed += 1
        total = sum(start_count.values())
        return total % (10**9 + 7)


class SolutionTest(TestCase):
    def test_one(self):
        self.assertEqual(Solution.knightDialer(0), 10)
        self.assertEqual(Solution.knightDialer(1), 10)
        self.assertEqual(Solution.knightDialer(2), 20)
        self.assertEqual(Solution.knightDialer(3), 46)
        self.assertEqual(Solution.knightDialer(4), 104)
