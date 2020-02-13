""" Find all the permutations of an array of unique integers
"""
from typing import List


class Solution(object):
    def __init__(self, input_array: List[int]):
        self.input_array = input_array
        self.length = len(input_array)
        self.indicies_scope = []
        self.permutations = []

    def figure_out_permutations(self):
        if self.indicies_scope.__len__() == self.length:
            perm = [self.input_array[index] for index in self.indicies_scope]
            self.permutations.append(perm)
            return

        for i, element in enumerate(self.input_array):
            if i not in self.indicies_scope:
                self.indicies_scope.append(i)
                self.figure_out_permutations()
                self.indicies_scope.pop(-1)

    def top_layer(self):
        self.figure_out_permutations()
        print(self.permutations)


