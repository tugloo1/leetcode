import random
from mock import patch
from unittest import TestCase
from typing import List


class Solution(object):
    def __init__(self, w: List[int]):
        self.original_weights = w
        self.cumulative_weights = [0]
        self.total = 0
        for weight in w:
            self.total += weight
            self.cumulative_weights.append(self.total)

    def pickIndex(self) -> int:
        random_int = random.randint(1, self.total)

        start = 0
        end = len(self.cumulative_weights) - 1

        while end - start > 1:
            middle_index = int((start + end)/2)
            middle_val = self.cumulative_weights[middle_index]
            if middle_val < random_int:
                start = middle_index
            else:
                end = middle_index
        return start

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


class SolutionTest(TestCase):
    def test_one(self):
        input1 = [10, 20, 40, 45, 15]
        s = Solution(input1)
        self.assertEqual(s.cumulative_weights, [0, 10, 30, 70, 115, 130])
        with patch('random.randint') as a:
            a.return_value = 1
            self.assertEqual(s.pickIndex(), 0)
            a.return_value = 11
            self.assertEqual(s.pickIndex(), 1)
            a.return_value = 128
            self.assertEqual(s.pickIndex(), 4)
