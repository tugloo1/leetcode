import heapq
from typing import List
from unittest import TestCase


class Solution:
    @classmethod
    def brute_force_approach(cls, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        meeting_assigments = []
        for interval in intervals:
            meeting_start = interval[0]
            for assignment in meeting_assigments:
                end_time = assignment[-1][1]
                if meeting_start >= end_time:
                    assignment.append(interval)
                    break
            else:
                meeting_assigments.append([interval])
        return len(meeting_assigments)

    @classmethod
    def heap_approach(cls, intervals: List[List[int]]) -> int:
        if intervals is []:
            return 0
        intervals.sort(key=lambda x: x[0])
        heap_container = []
        first_end_time = intervals[0][1]
        heapq.heappush(heap_container, first_end_time)
        for i in range(1, len(intervals)):
            start_time = intervals[i][0]
            end_time = intervals[i][1]
            if heap_container[0] <= start_time:
                heapq.heappop(heap_container)

            heapq.heappush(heap_container, end_time)

        return heap_container.__len__()


class SolutionTest(TestCase):
    def tests(self):
        a = [[0, 30], [5, 10], [15, 20]]
        self.assertEqual(Solution.heap_approach(a), 2)

    def test2(self):
        b = [[7, 10], [2, 4]]
        self.assertEqual(Solution.heap_approach(b), 1)

    def test3(self):
        a = [[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]
        self.assertEqual(Solution.heap_approach(a), 4)

