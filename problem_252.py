from typing import List
from unittest import TestCase


class Solution:
    @staticmethod
    def canAttendMeetings(intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        for i in range(len(intervals) - 1):
            next_start = intervals[i + 1][0]
            first_start = intervals[i][0]
            first_end = intervals[i][1]
            if next_start >= first_start and next_start < first_end:
                return False
        return True


class SolutionTest(TestCase):
    def test_one(self):
        a = [[0, 30], [5, 10], [15, 20]]
        self.assertFalse(Solution.canAttendMeetings(a))
        b = [[7,10],[2,4]]
        self.assertTrue(Solution.canAttendMeetings(b))
        c =  [[1, 13], [13, 15]]
        self.assertTrue(Solution.canAttendMeetings(c))
