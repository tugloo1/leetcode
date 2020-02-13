from typing import List
from unittest import TestCase


class SubSet(object):
    def __init__(self, inp: List[int]):
        self.inp = inp
        self.len = self.inp.__len__()
        self.subsets = []
        self.current_subset = []

    def get_solution(self):
        self.find_next_subset(0, False)
        return self.subsets

    def find_next_subset(self, next_index: int, right_side: bool):
        if not right_side:
            self.subsets.append(self.current_subset[:])

        if next_index < self.len:
            ss_index = next_index + 1
            self.current_subset.append(self.inp[next_index])
            self.find_next_subset(ss_index, False)
            self.current_subset.pop()
            self.find_next_subset(ss_index, True)


if __name__ == '__main__':
    s = SubSet([1, 2, 3])
    print(s.get_solution())

