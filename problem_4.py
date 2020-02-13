from unittest import TestCase
from typing import List


class Solution(object):
    @classmethod
    def findMedianSortedArrays(cls, array1: List[float], array2: List[float]):
        """
        :type array1: List[int]
        :type array2: List[int]
        :rtype: float
        """
        total_length = len(array1) + len(array2)
        even_length = total_length % 2 == 0
        if array1[0] <= array2[0]:
            first = array1
            second = array2
        else:
            first = array2
            second = array1
        # Non overlapping case
        median_index = int(total_length/2)
        if first[-1] <= second[0]:
            if median_index < len(first):
                if even_length:
                    return (first[median_index] + first[median_index - 1])/2
                else:
                    return first[median_index]
            else:
                median_index -= len(first)
                if even_length:
                    if median_index == 0:
                        return (second[median_index] + first[-1])/2
                    else:
                        return (second[median_index] + second[median_index - 1])/2
                    pass
                else:
                    return second[median_index]
        # Overlapping case
        if first[median_index] > second[0]:
            first_start = cls.binary_search_max_for_target(first, 0, len(first), second[0])
            first_end = cls.binary_search_max_for_target(first, first_start, len(first), second[-1])
            actual_first_end_index = first_end + len(second)
            while first_end - first_start != 1:
                midpoint = int((first_end + first_start)/2)
                midpoint_val = first[midpoint]
                second_c = cls.binary_search_max_for_target(second, 0, len(second), midpoint_val)
                actual_first_index = midpoint + second_c + 1
                if actual_first_index < median_index:
                    # move actual first_index to the right
                    first_start = midpoint
                else:
                    # Move actual first_index_to the left
                    first_end = midpoint
            print("")
        else:
            return first[median_index]


    @classmethod
    def binary_search_max_for_target(cls, inp_array, start, end, target):
        """ Find the target value for target using binary search
        :param inp_array:
        :param ind1:
        :param ind2:
        :param target:
        :return:
        """
        if target < inp_array[0]:
            return None

        while abs(start - end) != 1:
            middle_ind = int((start + end)/2)
            middle_val = inp_array[middle_ind]
            if middle_val > target:
                end = middle_ind
            else:
                start = middle_ind
        return start


class SolutionTest(TestCase):
    def test_non_overlapping_in_first_array(self):
        input1 = [1, 2, 3, 4, 5, 8]
        input2 = [8, 10, 11, 12, 15]
        self.assertEqual(Solution.findMedianSortedArrays(input1, input2), 8)
        self.assertEqual(Solution.findMedianSortedArrays(input2, input1), 8)
        input1 = [1, 2]
        input2 = [3, 4, 5, 6, 7]
        self.assertEqual(Solution.findMedianSortedArrays(input1, input2), 4)
        self.assertEqual(Solution.findMedianSortedArrays(input2, input1), 4)
        # Even numbers
        input1 = [1, 2, 3, 4]
        input2 = [5, 6]
        self.assertEqual(Solution.findMedianSortedArrays(input1, input2), 3.5)
        self.assertEqual(Solution.findMedianSortedArrays(input2, input1), 3.5)
        input1 = [1, 2]
        input2 = [3, 4]
        self.assertEqual(Solution.findMedianSortedArrays(input1, input2), 2.5)
        self.assertEqual(Solution.findMedianSortedArrays(input2, input1), 2.5)

    def test_binary_search_array_for_value(self):
        input1 = [4, 9, 11, 15, 18, 20, 21, 24]
        size = len(input1)
        valid_inputs = [16, 12, 11, 2, 25]
        valid_outputs = [3, 2, 2, None, 7]
        for i, inp in enumerate(valid_inputs):
            self.assertEqual(Solution.binary_search_max_for_target(input1, 0, size, inp), valid_outputs[i])

        input2 = [3, 10]
        inputs = [-1, 5, 11]
        valid_outputs = [None, 0, 1]
        for i, inp in enumerate(inputs):
            self.assertEqual(Solution.binary_search_max_for_target(input2, 0, len(input2), inp), valid_outputs[i])

    def test_subrange_median_array_odd(self):
        # input1 = [1, 3]
        # input2 = [2]
        # self.assertEqual(Solution.findMedianSortedArrays(input1, input2), 2)
        input1 = [4, 9, 11, 15, 18, 20, 21, 24]
        input2 = [16, 19, 20, 22, 23]
        correct_value = 19
        self.assertEqual(Solution.findMedianSortedArrays(input1, input2), correct_value)
        input1 = [4, 9, 11, 15, 18, 19, 21, 24]
        input2 = [16, 20, 20, 22, 23]
        correct_value = 19
        self.assertEqual(Solution.findMedianSortedArrays(input1, input2), correct_value)

    def test_subrange_median_array_even(self):
        input1 = [4, 9, 11, 15, 18, 20, 21, 24, 25]
        input2 = [16, 19, 20, 22, 23]
        correct_value = 19.5
        self.assertEqual(Solution.findMedianSortedArrays(input1, input2), correct_value)
