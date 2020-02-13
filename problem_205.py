from unittest import TestCase


class Solution:

    @staticmethod
    def convert_string_to_isomorphic(input_string: str) -> str:
        old_to_new_map = {}
        next_letter_ascii = ord('a')
        new_string = ''

        for char in input_string:
            if char in old_to_new_map:
                new_string += old_to_new_map[char]
            else:
                new_char = chr(next_letter_ascii)
                new_string += new_char
                old_to_new_map[char] = new_char
                next_letter_ascii += 1
        return new_string

    def isIsomorphic(self, first: str, second: str) -> bool:
        new_first = self.convert_string_to_isomorphic(first)
        new_second = self.convert_string_to_isomorphic(second)
        return new_first == new_second


class SolutionTest(TestCase):
    def test_one(self):
        s = Solution()
        self.assertTrue(s.isIsomorphic('egg', 'add'))
        self.assertFalse(s.isIsomorphic('foo', 'bar'))
        self.assertTrue(s.isIsomorphic('paper', 'title'))
        self.assertFalse(s.isIsomorphic('aaabbbb', 'cdcdcd'))
