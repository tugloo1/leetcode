from typing import List
from unittest import TestCase


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums)
        # case where it's unsorted
        if nums[0] < nums[-1]:
            return nums[0]

        i, j = 0, len(nums) - 1
        first = nums[0]
        while j - i > 1:
            mid_point = int((i+j)/2)
            if nums[mid_point] < first:
                j = mid_point
                pass
            else:
                i = mid_point
                pass
        return min(nums[i], nums[j])


class SolutionTest(TestCase):
    def test1(self):
        s = Solution()
        self.assertEqual(0, s.findMin([1, 2, 3, 4, 5, 0]))
        self.assertEqual(0, s.findMin([2, 3, 4, 5, 0, 1]))
        self.assertEqual(0, s.findMin([3, 4, 5, 0, 1, 2]))
        self.assertEqual(0, s.findMin([4, 5, 0, 1, 2, 3]))
