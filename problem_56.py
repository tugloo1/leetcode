from typing import List
from unittest import TestCase


class Solution:
    @staticmethod
    def merge(intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]
        for interval in intervals[1:]:
            interval_start, interval_end = interval
            if interval_start <= output[-1][1]:
                old_interval = output.pop()
                new_interval = [old_interval[0], max(interval_end, old_interval[1])]
                output.append(new_interval)
            else:
                output.append(interval)
        return output


class SolutionTest(TestCase):
    def tests(self):
        a = [[1,3],[2,6],[8,10],[15,18]]
        self.assertEqual(Solution.merge(a), [[1,6],[8,10],[15,18]])
        b = [[1,4],[4,5]]
        self.assertEqual(Solution.merge(b),  [[1,5]])
        c = [[1,4],[2,3]]
        self.assertEqual(Solution.merge(c), [[1, 4]])
