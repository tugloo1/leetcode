from unittest import TestCase


class Solution:
    @staticmethod
    def climbStairs(n: int) -> int:
        if n == 1:
            return 1
        two_steps_back = 1
        one_step_back = 2
        possibilities = 2

        current_step = 3
        while current_step <= n:
            possibilities = two_steps_back + one_step_back
            two_steps_back = one_step_back
            one_step_back = possibilities
            current_step += 1
        return possibilities




class SolutionTest(TestCase):
    def test_sol(self):
        self.assertEqual(Solution.climbStairs(2), 2)
        self.assertEqual(Solution.climbStairs(3), 3)
