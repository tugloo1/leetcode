from unittest import TestCase
from typing import List, Dict


class Solution:
    @staticmethod
    def is_str1_first(str1: str, str2: str, order_map: Dict[str, int]):
        len1 = len(str1)
        len2 = len(str2)
        for i, _ in enumerate(str1):
            # case where i exceeds
            if i >= len2:
                return False
            if str1[i] == str2[i]:
                continue
            value1, value2 = order_map[str1[i]], order_map[str2[i]]
            if value1 < value2:
                return True
            elif value1 > value2:
                return False
            elif value1 == value2:
                continue
        if len2 > len1:
            return True

    @staticmethod
    def isAlienSorted(words: List[str], order: str) -> bool:
        order_map = {char: i for i, char in enumerate(order)}
        for i in range(len(words) - 1):
            if not Solution.is_str1_first(words[i], words[i+1], order_map):
                return False
        return True


class SolutionTest(TestCase):
    def test1(self):
        words = ["hello", "leetcode"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        self.assertTrue(Solution.isAlienSorted(words, order))

    def test2(self):
        words = ["word", "world", "row"]
        order = "worldabcefghijkmnpqstuvxyz"
        self.assertFalse(Solution.isAlienSorted(words, order))

    def test3(self):
        words = ["apple", "app"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertFalse(Solution.isAlienSorted(words, order))

