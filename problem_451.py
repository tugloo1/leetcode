import heapq
from unittest import TestCase


class Solution:
    @staticmethod
    def frequencySort(s: str) -> str:
        freq_count = {}
        for char in s:
            if char in freq_count:
                freq_count[char] += 1
            else:
                freq_count[char] = 1
        priority_q = []
        for char in freq_count:
            tup = (-1*freq_count[char], char)
            heapq.heappush(priority_q, tup)

        output = ''
        for i in range(len(priority_q)):
            tup = heapq.heappop(priority_q)
            output += tup[1] * (tup[0]*-1)
        return output


class SolutionTest(TestCase):
    def tests(self):
        s = 'ddabbbbbccc'
        self.assertEqual(Solution.frequencySort(s), 'bbbbbcccdda')

