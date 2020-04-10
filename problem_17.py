from unittest import TestCase
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        maps = {'2': 'abc', '3': 'def',
                '4': 'ghi', '5': 'jkl',
                '6': 'mno', '7': 'pqrs',
                '8': 'tuv', '9': 'wxyz'}
        output = list(maps[digits[-1]])
        if len(digits) == 1:
            return output
        digits = digits[:-1]
        for digit in reversed(digits):
            new_output = []
            for character in maps[digit]:
                for o in output:
                    new_value = character + o
                    new_output.append(new_value)
            output = new_output
        return output


class SolutionTest(TestCase):
    def test_one(self):
        valid = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        inp = "23"
        s = Solution()
        o = s.letterCombinations(inp)
        self.assertEqual(o, valid)

