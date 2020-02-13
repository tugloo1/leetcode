from typing import List
from unittest import TestCase


class Solution:
    @staticmethod
    def canPartition(nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = int(total/2)
        last_vector = [0] * (half + 1)

        for item_index in range(0, len(nums)):
            item_weight = nums[item_index]
            current = last_vector.copy()
            for max_weight_allowed in range(item_weight, half + 1):
                max_weight_without_current = max_weight_allowed - item_weight
                last_max_weight = last_vector[max_weight_without_current]
                max_weight_with_current =  last_vector[max_weight_allowed]
                pos_new_weight = last_max_weight + item_weight
                if pos_new_weight > max_weight_with_current:
                    current[max_weight_allowed] = pos_new_weight
                if pos_new_weight == half:
                    return True

            last_vector = current
        return False


class SolutionTest(TestCase):
    def test_a(self):
        a = [1, 5, 11, 5]
        self.assertTrue(Solution.canPartition(a))

    def test_b(self):
        b = [1, 2, 3, 5]
        self.assertFalse(Solution.canPartition(b))
