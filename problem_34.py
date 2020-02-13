from typing import List
from unittest import TestCase


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        not_found = [-1, -1]
        if not nums or nums[0] > target or target > nums[-1]:
            return not_found
        start, end = 0, len(nums) - 1
        index_found = self.binary_search_inclusive(nums, target, start, end)
        if index_found == -1:
            return not_found

        start_position, end_position = index_found, index_found
        while start_position > 0 and nums[start_position - 1] == target:
            start_position = self.binary_search_inclusive(nums, target, start, start_position - 1)

        while end_position < end and nums[end_position + 1] == target:
            end_position = self.binary_search_inclusive(nums, target, end_position + 1, end)
        return [start_position, end_position]

    @staticmethod
    def binary_search_inclusive(nums: List[int], target: int, start: int, end: int):
        while end - start > 1:
            mid_index = int((start + end)/2)
            mid_val = nums[mid_index]
            if mid_val == target:
                return mid_index
            if mid_val > target:
                end = mid_index
            else:
                start = mid_index
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1


class SolutionTest(TestCase):
    def test_search_range(self):
        s = Solution()
        nums = [5, 7, 7, 8, 8, 10]
        target = 3
        self.assertEqual(s.searchRange(nums, target), [-1, -1])
        target = 11
        self.assertEqual(s.searchRange(nums, target), [-1, -1])
        target = 6
        self.assertEqual(s.searchRange(nums, target), [-1, -1])
        target = 8
        self.assertEqual(s.searchRange(nums, target), [3, 4])
