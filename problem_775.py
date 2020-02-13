from unittest import TestCase
from typing import List, Tuple


class MergeSort(object):
    def __init__(self, input_list):
        self.input_list = input_list

    def sort(self):
        return self._rec_split_merge_and_sort(self.input_list)

    def _rec_split_merge_and_sort(self, input_list: List[int]):
        array_length = len(input_list)
        # Base case for recursion
        if array_length == 1:
            return input_list
        half_way = int(array_length/2)
        left_half = input_list[:half_way]
        right_half = input_list[half_way:]
        sorted_left = self._rec_split_merge_and_sort(left_half)
        sorted_right = self._rec_split_merge_and_sort(right_half)
        left_len = len(sorted_left)
        right_len = len(sorted_right)
        i, j = 0, 0
        merged_array = []
        for k in range(array_length):
            if sorted_left[i] < sorted_right[j]:
                merged_array.append(sorted_left[i])
                i += 1
            else:
                merged_array.append(sorted_right[j])
                j += 1
            if i == left_len:
                merged_array += sorted_right[j:]
                break
            elif j == right_len:
                merged_array += sorted_left[i:]
                break
        return merged_array

    def count_inversions(self):
        _, count = self._count_inversions(self.input_list)
        return count

    def _count_inversions(self, input_list: List[int]) -> Tuple[List[int], int]:
        total_len = input_list.__len__()
        if total_len == 1:
            return input_list, 0
        half_way = int(total_len/2)
        l_half = input_list[:half_way]
        r_half = input_list[half_way:]
        sorted_left, l_invs = self._count_inversions(l_half)
        sorted_right, r_invs = self._count_inversions(r_half)

        left_len, right_len = l_half.__len__(), r_half.__len__()
        i, j, split_inv = 0, 0, 0
        merged_array = []
        for k in range(total_len):
            if sorted_left[i] < sorted_right[j]:
                merged_array.append(sorted_left[i])
                i += 1
            else:
                merged_array.append(sorted_right[j])
                j += 1
                split_inv += left_len - i
            if i == left_len:
                merged_array += sorted_right[j:]
                break
            if j == right_len:
                merged_array += sorted_left[i:]
                break
        total_invs = l_invs + r_invs + split_inv
        return merged_array, total_invs


class Solution(object):
    @staticmethod
    def get_num_of_local_invs(inp_list: List[int]):
        num = 0
        for i in range(inp_list.__len__() - 1):
            if inp_list[i] > inp_list[i + 1]:
                num += 1
        return num

    def isIdealPermutation(self, A: List[int]) -> bool:
        local_invs = self.get_num_of_local_invs(A)
        merge_sort = MergeSort(A)
        global_invs = merge_sort.count_inversions()
        return local_invs == global_invs


class SolutionTest(TestCase):
    def test_one(self):
        sol = Solution()
        o = sol.isIdealPermutation([0])
        self.assertTrue(o)
        o = sol.isIdealPermutation([1, 0])
        self.assertTrue(o)