from unittest import TestCase


class Solution:
    @staticmethod
    def numJewelsInStones(J: str, S: str) -> int:
        jewels = {stone for stone in J}
        count = 0
        for p in S:
            if p in jewels:
                count += 1
        return count



class SolutionTest(TestCase):
    def test_numJewelsInStones(self):
        j = 'aA'
        s = 'aAAbbbb'
        self.assertEqual(Solution.numJewelsInStones(j, s), 3)
