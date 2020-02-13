from unittest import TestCase


class Solution:
    @staticmethod
    def isSubsequence(s: str, t: str) -> bool:
        if not s:
            return True
        s_i = 0  # Subsequence
        t_i = 0
        while t_i < len(t):
            s_selected = s[s_i]
            t_selected = t[t_i]
            if s_selected == t_selected:
                s_i += 1
                if s_i == len(s):
                    return True
            t_i += 1
        return False


class SolutionTest(TestCase):
    def test_is_ss(self):
        self.assertTrue(Solution.isSubsequence("abc", "ahbgdc"))
        self.assertFalse(Solution.isSubsequence("acb", "ahbgdc"))
