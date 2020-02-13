from typing import List
from unittest import TestCase


class SubsetFinder(object):
    def __init__(self, inp: List[int]):
        self.inp = inp
        self.inp.sort()
        self.subset_map = {}
        self.len = self.inp.__len__()
        self.tracking_subset = []

    def get_subset_main(self):
        self._get_subset(0, False)
        # output = set(self.subset)
        final_output = []
        for key in self.subset_map.keys():
            for s in self.subset_map[key]:
                final_output.append(list(s))

        return final_output

    def _get_subset(self, next_index: int, right_side: bool):
        if not right_side:
            tracking_subset_len = self.tracking_subset.__len__()
            fz = tuple(self.tracking_subset)
            if tracking_subset_len not in self.subset_map:
                self.subset_map[tracking_subset_len] = set()
            self.subset_map[tracking_subset_len].add(fz)

        if next_index < self.len:
            value = self.inp[next_index]
            self.tracking_subset.append(value)
            self._get_subset(next_index + 1, False)
            self.tracking_subset.pop(-1)
            self._get_subset(next_index + 1, True)


class SolutionTest(TestCase):
    def check_equal(self, inp: List[int], valid_answer: List[List[int]]):
        i = SubsetFinder(inp)
        seen = i.get_subset_main()
        self.assertEqual(seen.__len__(), valid_answer.__len__())
        for i in valid_answer:
            self.assertIn(i, seen)

    def test1(self):
        inp = [1, 2, 2]
        correct = [[2], [1], [1, 2, 2], [2, 2], [1, 2], []]
        self.check_equal(inp, correct)

    def test2(self):
        inp = [4, 4, 4, 1, 4]
        correct = [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]
        self.check_equal(inp, correct)

